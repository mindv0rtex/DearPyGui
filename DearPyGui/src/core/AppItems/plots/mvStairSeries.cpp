#include <utility>
#include "mvStairSeries.h"
#include "mvCore.h"
#include "mvApp.h"
#include "mvItemRegistry.h"
#include "mvImPlotThemeScope.h"

namespace Marvel {

	void mvStairSeries::InsertParser(std::map<std::string, mvPythonParser>* parsers)
	{

		parsers->insert({ s_command, mvPythonParser({
			{mvPythonDataType::Optional},
			{mvPythonDataType::String, "name"},
			{mvPythonDataType::KeywordOnly},
			{mvPythonDataType::FloatList, "x"},
			{mvPythonDataType::FloatList, "y"},
			{mvPythonDataType::String, "label", "Overrides 'name' as label", "''"},
			{mvPythonDataType::String, "source", "", "''"},
			{mvPythonDataType::String, "parent", "Parent to add this item to. (runtime adding)", "''"},
			{mvPythonDataType::String, "before", "This item will be displayed before the specified item in the parent. (runtime adding)", "''"},
			{mvPythonDataType::Bool, "show", "Attempt to render", "True"},
			{mvPythonDataType::Integer, "axis", "", "0"},
			{mvPythonDataType::Bool, "contribute_to_bounds", "", "True"},
		}, "Adds a drag point to a plot.", "None", "Plotting") });
	}

	mvStairSeries::mvStairSeries(const std::string& name)
		: mvSeriesBase(name)
	{
	}

	void mvStairSeries::draw(ImDrawList* drawlist, float x, float y)
	{
		ScopedID id;
		mvImPlotThemeScope scope(this);

		switch (m_axis)
		{
		case ImPlotYAxis_1:
			ImPlot::SetPlotYAxis(ImPlotYAxis_1);
			break;
		case ImPlotYAxis_2:
			ImPlot::SetPlotYAxis(ImPlotYAxis_2);
			break;
		case ImPlotYAxis_3:
			ImPlot::SetPlotYAxis(ImPlotYAxis_3);
			break;
		default:
			break;
		}

		static const std::vector<float>* xptr;
		static const std::vector<float>* yptr;

		xptr = &(*m_value.get())[0];
		yptr = &(*m_value.get())[1];

		ImPlot::PlotStairs(m_label.c_str(), xptr->data(), yptr->data(), xptr->size());

	}

	void mvStairSeries::setExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;

		if (PyObject* item = PyDict_GetItemString(dict, "axis")) m_axis = (ImPlotYAxis_)ToInt(item);
		if (PyObject* item = PyDict_GetItemString(dict, "contribute_to_bounds")) m_contributeToBounds = ToBool(item);

		bool valueChanged = false;
		if (PyObject* item = PyDict_GetItemString(dict, "x")) { valueChanged = true; (*m_value)[0] = ToFloatVect(item); }
		if (PyObject* item = PyDict_GetItemString(dict, "y")) { valueChanged = true; (*m_value)[1] = ToFloatVect(item); }

		if (valueChanged)
		{
			resetMaxMins();
			calculateMaxMins();
		}
	}

	void mvStairSeries::getExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;
	}

}