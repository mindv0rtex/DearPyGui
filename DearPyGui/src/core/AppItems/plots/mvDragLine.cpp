#include <utility>
#include "mvDragLine.h"
#include "mvCore.h"
#include "mvApp.h"
#include "mvLog.h"
#include "mvItemRegistry.h"
#include "mvFontScope.h"

namespace Marvel {

	void mvDragLine::InsertParser(std::map<std::string, mvPythonParser>* parsers)
	{

		parsers->insert({ s_command, mvPythonParser({
			{mvPythonDataType::Optional},
			{mvPythonDataType::String, "name"},
			{mvPythonDataType::KeywordOnly},
			{mvPythonDataType::FloatList, "default_value", "", "(0.0, 0.0, 0.0, 0.0)"},
			{mvPythonDataType::String, "label", "Overrides 'name' as label", "''"},
			{mvPythonDataType::String, "source", "", "''"},
			{mvPythonDataType::FloatList, "color", "", "(0, 0, 0, -1)"},
			{mvPythonDataType::Float, "thickness", "", "1.0"},
			{mvPythonDataType::Bool, "show_label", "", "True"},
			{mvPythonDataType::Bool, "vertical", "", "True"},
			{mvPythonDataType::Callable, "callback", "function to run when point is moved", "None"},
			{mvPythonDataType::String, "parent", "Parent to add this item to. (runtime adding)", "''"},
			{mvPythonDataType::String, "before", "This item will be displayed before the specified item in the parent. (runtime adding)", "''"},
			{mvPythonDataType::Bool, "show", "Attempt to render", "True"},
		}, "Adds a drag point to a plot.", "None", "Plotting") });
	}

	mvDragLine::mvDragLine(const std::string& name)
		: mvFloatPtrBase(name)
	{
	}

	bool mvDragLine::isParentCompatible(mvAppItemType type)
	{
		if (type == mvAppItemType::mvPlot)
			return true;

		mvThrowPythonError(1000, "Item's parent must be plot.");
		MV_ITEM_REGISTRY_ERROR("Item's parent must be plot.");
		assert(false);
		return false;
	}

	void mvDragLine::draw(ImDrawList* drawlist, float x, float y)
	{
		ScopedID id;
		mvFontScope fscope(this);

		static double dummy = 0.0;
		dummy = *(float*)m_value.get();

		if (m_vertical)
		{
			if (ImPlot::DragLineX(m_label.c_str(), &dummy, m_show_label, m_color, m_thickness))
			{
				*m_value.get() = (float)dummy;
				mvApp::GetApp()->getCallbackRegistry().addCallback(m_callback, m_name, nullptr);
			}
		}
		else
		{
			if (ImPlot::DragLineY(m_label.c_str(), &dummy, m_show_label, m_color, m_thickness))
			{
				*m_value.get() = (float)dummy;
				mvApp::GetApp()->getCallbackRegistry().addCallback(m_callback, m_name, nullptr);
			}
		}

	}

	void mvDragLine::setExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;

		if (PyObject* item = PyDict_GetItemString(dict, "color")) m_color = ToColor(item);
		if (PyObject* item = PyDict_GetItemString(dict, "thickness")) m_thickness = ToFloat(item);
		if (PyObject* item = PyDict_GetItemString(dict, "show_label")) m_show_label = ToBool(item);
		if (PyObject* item = PyDict_GetItemString(dict, "vertical")) m_vertical = ToBool(item);

	}

	void mvDragLine::getExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;
	}

}