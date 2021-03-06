#include "mvMenu.h"
#include "mvApp.h"
#include "mvItemRegistry.h"
#include "mvImGuiThemeScope.h"
#include "mvFontScope.h"

namespace Marvel {

	void mvMenu::InsertParser(std::map<std::string, mvPythonParser>* parsers)
	{
		parsers->insert({ s_command, mvPythonParser({
			{mvPythonDataType::Optional},
			{mvPythonDataType::String, "name"},
			{mvPythonDataType::KeywordOnly},
			{mvPythonDataType::String, "label", "", "''"},
			{mvPythonDataType::Bool, "show", "Attempt to render", "True"},
			{mvPythonDataType::String, "parent", "Parent this item will be added to. (runtime adding)", "''"},
			{mvPythonDataType::String, "before", "This item will be displayed before the specified item in the parent. (runtime adding)", "''"},
			{mvPythonDataType::Bool, "enabled", "", "True"},
		}, "Adds a menu to an existing menu bar. Must be followed by a call to end.", "None", "Containers") });
	}

	mvMenu::mvMenu(const std::string& name)
			: mvBoolPtrBase(name)
	{
	}

	void mvMenu::draw(ImDrawList* drawlist, float x, float y)
	{
		ScopedID id;
		mvImGuiThemeScope scope(this);
		mvFontScope fscope(this);

		// create menu and see if its selected
		if (ImGui::BeginMenu(m_label.c_str(), m_enabled))
		{

			// set other menus's value false on same level
			for (auto sibling : m_parentPtr->m_children[1])
			{
				// ensure sibling
				if (sibling->getType() == mvAppItemType::mvMenu)
					*((mvMenu*)sibling.get())->m_value = false;
			}

			// set current menu value true
			*m_value = true;

			//we do this so that the children dont get the theme
			scope.cleanup();

			for (auto& item : m_children[1])
			{
				// skip item if it's not shown
				if (!item->m_show)
					continue;

				// set item width
				if (item->m_width != 0)
					ImGui::SetNextItemWidth((float)item->m_width);

				item->draw(drawlist, ImGui::GetCursorPosX(), ImGui::GetCursorPosY());

				item->getState().update();
			}

			registerWindowFocusing();

			ImGui::EndMenu();
		}

	}

	void mvMenu::setExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;
		 
		if (PyObject* item = PyDict_GetItemString(dict, "enabled")) m_enabled = ToBool(item);

	}

	void mvMenu::getExtraConfigDict(PyObject* dict)
	{
		if (dict == nullptr)
			return;
		 
		PyDict_SetItemString(dict, "enabled", ToPyBool(m_enabled));
	}

}