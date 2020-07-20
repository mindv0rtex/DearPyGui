from typing import List, Any

def add_button(name: str, small: bool, arrow: bool, direction: int, callback: str, tip: str, parent: str, before: str, width: int, height: int) -> None:
	"""Adds a button."""
	...

def add_checkbox(name: str, default_value: int, callback: str, tip: str, parent: str, before: str, data_source: str) -> None:
	"""Adds a checkbox widget."""
	...

def add_child(name: str, tip: str, parent: str, before: str, width: int, height: int, border: bool) -> None:
	"""Adds an embedded child window. Will show scrollbars when items do not fit. Must be followed by a call to end_child."""
	...

def add_collapsing_header(name: str, default_open: bool, closable: bool, tip: str, parent: str, before: str) -> None:
	"""Adds a collapsing header to add items to. Must be closed with the end_collapsing_header command."""
	...

def add_color_edit3(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds an rgb color editing widget."""
	...

def add_color_edit4(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds an rgba color editing widget."""
	...

def add_color_picker3(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds an rgb color picking widget."""
	...

def add_color_picker4(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds an rgba color picking widget."""
	...

def add_column(table: str, name: str, column: List[str]) -> None:
	"""Adds a column to a table."""
	...

def add_combo(name: str, items: List[str], default_value: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int, secondary_data_source: str) -> None:
	"""Adds a combo."""
	...

def add_data(name: str, data: object) -> None:
	"""Adds data for later retrieval."""
	...

def add_drag_float(name: str, default_value: float, speed: float, min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a single float value"""
	...

def add_drag_float2(name: str, default_value: List[float], speed: float, min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 2 float values."""
	...

def add_drag_float3(name: str, default_value: List[float], speed: float, min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 3 float values."""
	...

def add_drag_float4(name: str, default_value: List[float], speed: float, min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 4 float values."""
	...

def add_drag_int(name: str, default_value: int, speed: float, min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a single int value"""
	...

def add_drag_int2(name: str, default_value: List[int], speed: float, min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 2 int values."""
	...

def add_drag_int3(name: str, default_value: List[int], speed: float, min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 3 int values."""
	...

def add_drag_int4(name: str, default_value: List[int], speed: float, min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds drag for a 4 int values."""
	...

def add_drawing(name: str, tip: str, parent: str, before: str, width: int, height: int) -> None:
	"""Adds a drawing widget."""
	...

def add_group(name: str, tip: str, parent: str, before: str, width: int) -> None:
	"""Creates a group that other widgets can belong to. The group allows item commands to be issued for all of its members.				Must be closed with the end_group command unless added at runtime."""
	...

def add_image(name: str, value: str, tint_color: List[float], border_color: List[float], tip: str, parent: str, before: str, data_source: str, width: int, height: int, uv_min: List[float], uv_max: List[float], secondary_data_source: str) -> None:
	"""Adds an image."""
	...

def add_indent(name: str, offset: float, parent: str, before: str) -> None:
	"""Adds an indent to following items."""
	...

def add_input_float(name: str, default_value: float, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for float values."""
	...

def add_input_float2(name: str, default_value: List[float], format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 2 float values."""
	...

def add_input_float3(name: str, default_value: List[float], format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 3 float values."""
	...

def add_input_float4(name: str, default_value: List[float], format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 4 float values."""
	...

def add_input_int(name: str, default_value: int, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for integer values."""
	...

def add_input_int2(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 2 integer values."""
	...

def add_input_int3(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 3 integer values."""
	...

def add_input_int4(name: str, default_value: List[int], callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for 4 integer values."""
	...

def add_input_text(name: str, default_value: str, hint: str, multiline: bool, no_spaces: bool, uppercase: bool, decimal: bool, hexadecimal: bool, readonly: bool, password: bool, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds input for text values."""
	...

def add_item_color_style(item: str, style: int, color: List[float]) -> None:
	"""Needs documentation"""
	...

def add_label_text(name: str, value: str, color: List[float], tip: str, parent: str, before: str, data_source: str) -> None:
	"""Adds text with a label. Useful for output values."""
	...

def add_line_series(plot: str, name: str, data: List[float], color: List[float], fill: List[float], weight: float) -> None:
	"""Adds a line series to a plot."""
	...

def add_listbox(name: str, items: List[str], default_value: int, callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int, secondary_data_source: str) -> None:
	"""Adds a listbox."""
	...

def add_menu(name: str, tip: str, parent: str, before: str) -> None:
	"""Adds a menu to an existing menu bar. Must be followed by a call to end_menu."""
	...

def add_menu_bar(name: str, parent: str, before: str) -> None:
	"""Adds a menu bar to a window. Must be followed by a call to end_menu_bar."""
	...

def add_menu_item(name: str, callback: str, tip: str, parent: str, before: str) -> None:
	"""Adds a menu item to an existing menu."""
	...

def add_plot(name: str, xAxisName: str, yAxisName: str, flags: int, xflags: int, yflags: int, parent: str, before: str, width: int, height: int, query_callback: str) -> None:
	"""Adds a plot widget."""
	...

def add_popup(popupparent: str, name: str, mousebutton: int, modal: bool, parent: str, before: str, width: int, height: int) -> None:
	"""Adds a popup window for an item. This command must come immediately after the item the popup is for."""
	...

def add_progress_bar(name: str, value: float, overlay: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds a progress bar."""
	...

def add_radio_button(name: str, items: List[str], default_value: int, callback: str, tip: str, parent: str, before: str, data_source: str, secondary_data_source: str) -> None:
	"""Adds a set of radio buttons."""
	...

def add_row(table: str, row: List[str]) -> None:
	"""Adds a row to a table."""
	...

def add_same_line(name: str, xoffset: float, spacing: float, parent: str, before: str) -> None:
	"""Places a widget on the same line as the previous widget. Can also be used for horizontal spacing."""
	...

def add_scatter_series(plot: str, name: str, data: List[float], marker: int, size: float, weight: float, outline: List[float], fill: List[float]) -> None:
	"""Adds a scatter series to a plot."""
	...

def add_selectable(name: str, default_value: bool, callback: str, tip: str, parent: str, before: str, data_source: str) -> None:
	"""Adds a selectable."""
	...

def add_seperator(name: str, tip: str, parent: str, before: str) -> None:
	"""Adds a horizontal line."""
	...

def add_simple_plot(name: str, value: List[float], autoscale: bool, overlay: str, minscale: float, maxscale: float, histogram: bool, tip: str, parent: str, before: str, width: int, height: int) -> None:
	"""A simple plot for visualization of a set of values"""
	...

def add_slider_float(name: str, default_value: float, min_value: float, max_value: float, format: str, power: float, vertical: bool, callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds slider for a single float value"""
	...

def add_slider_float2(name: str, default_value: List[float], min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 2 float values."""
	...

def add_slider_float3(name: str, default_value: List[float], min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 3 float values."""
	...

def add_slider_float4(name: str, default_value: List[float], min_value: float, max_value: float, format: str, power: float, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 4 float values."""
	...

def add_slider_int(name: str, default_value: int, min_value: int, max_value: int, format: str, vertical: bool, callback: str, tip: str, parent: str, before: str, data_source: str, width: int, height: int) -> None:
	"""Adds slider for a single int value"""
	...

def add_slider_int2(name: str, default_value: List[int], min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 2 int values."""
	...

def add_slider_int3(name: str, default_value: List[int], min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 3 int values."""
	...

def add_slider_int4(name: str, default_value: List[int], min_value: int, max_value: int, format: str, callback: str, tip: str, parent: str, before: str, data_source: str, width: int) -> None:
	"""Adds slider for a 4 int values."""
	...

def add_spacing(name: str, count: int, parent: str, before: str) -> None:
	"""Adds vertical spacing."""
	...

def add_tab(name: str, closable: bool, tip: str, parent: str, before: str) -> None:
	"""Adds a tab to a tab bar."""
	...

def add_tab_bar(name: str, reorderable: bool, callback: str, parent: str, before: str, data_source: str) -> None:
	"""Adds a tab bar."""
	...

def add_table(name: str, headers: List[str], callback: str, parent: str, before: str) -> None:
	"""Adds table."""
	...

def add_text(name: str, wrap: int, color: List[float], bullet: bool, tip: str, parent: str, before: str) -> None:
	"""Adds text"""
	...

def add_text_point(plot: str, name: str, x: float, y: float, vertical: bool, xoffset: int, yoffset: int) -> None:
	"""Adds a point with text to a plot."""
	...

def add_tooltip(tipparent: str, name: str, parent: str, before: str) -> None:
	"""Adds an advanced tool tip for an item. This command must come immediately after the item the tip is for."""
	...

def add_tree_node(name: str, default_open: bool, tip: str, parent: str, before: str) -> None:
	"""Adds a tree node to add items to. Must be closed with the end_tree_node command."""
	...

def add_window(name: str, width: int, height: int, start_x: int, start_y: int, autosize: bool, resizable: bool, title_bar: bool, movable: bool, hide: bool) -> None:
	"""Creates a new window for following items to be added to. Must call end_main_window command before."""
	...

def change_style_item(item: int, x: float, y: float) -> None:
	"""Needs documentation"""
	...

def change_theme_item(item: int, r: float, g: float, b: float, a: float) -> None:
	"""Needs documentation"""
	...

def clear_drawing(draw: str) -> None:
	"""Clears a drawing."""
	...

def clear_log() -> None:
	"""Clears the logger."""
	...

def clear_plot(plot: str) -> None:
	"""Clears a plot."""
	...

def close_popup() -> None:
	"""Needs documentation"""
	...

def delete_column(table: str, column: int) -> None:
	"""Delete a column in a table."""
	...

def delete_data(name: str) -> None:
	"""Deletes data from storage."""
	...

def delete_item(item: str, children_only: bool) -> None:
	"""Deletes an item if it exists."""
	...

def delete_row(table: str, row: int) -> None:
	"""Delete a row in a table."""
	...

def draw_arrow(drawing: str, p1: List[float], p2: List[float], color: List[int], thickness: int, size: int, tag: str) -> None:
	"""Draws an arrow on a drawing."""
	...

def draw_bezier_curve(drawing: str, p1: List[float], p2: List[float], p3: List[float], p4: List[float], color: List[int], thickness: float, segments: int, tag: str) -> None:
	"""Draws a bezier curve on a drawing."""
	...

def draw_circle(drawing: str, center: List[float], radius: float, color: List[int], segments: int, thickness: float, fill: List[float], tag: str) -> None:
	"""Draws a circle on a drawing."""
	...

def draw_image(drawing: str, file: str, pmin: List[float], pmax: List[float], uv_min: List[float], uv_max: List[float], color: List[int], tag: str) -> None:
	"""Draws an image on a drawing."""
	...

def draw_line(drawing: str, p1: List[float], p2: List[float], color: List[int], thickness: int, tag: str) -> None:
	"""Draws a line on a drawing."""
	...

def draw_polygon(drawing: str, points: List[float], color: List[int], fill: List[float], thickness: float, tag: str) -> None:
	"""Draws a polygon on a drawing."""
	...

def draw_polyline(drawing: str, points: List[float], color: List[int], closed: int, thickness: float, tag: str) -> None:
	"""Draws lines on a drawing."""
	...

def draw_quad(drawing: str, p1: List[float], p2: List[float], p3: List[float], p4: List[float], color: List[int], fill: List[float], thickness: float, tag: str) -> None:
	"""Draws a quad on a drawing."""
	...

def draw_rectangle(drawing: str, pmin: List[float], pmax: List[float], color: List[int], fill: List[float], rounding: float, thickness: float, tag: str) -> None:
	"""Draws a rectangle on a drawing."""
	...

def draw_text(drawing: str, pos: List[float], text: str, color: List[int], size: int, tag: str) -> None:
	"""Draws text on a drawing."""
	...

def draw_triangle(drawing: str, p1: List[float], p2: List[float], p3: List[float], color: List[int], fill: List[float], thickness: float, tag: str) -> None:
	"""Draws a triangle on a drawing."""
	...

def end_child() -> None:
	"""Ends the child created by a call to add_child."""
	...

def end_collapsing_header() -> None:
	"""Ends the collapsing header created by a call to add_collapsing_header."""
	...

def end_group() -> None:
	"""Ends the group created by a call to add_group."""
	...

def end_menu() -> None:
	"""Ends the menu created by a call to add_menu."""
	...

def end_menu_bar() -> None:
	"""Ends the menu bar created by a call to add_menu_bar."""
	...

def end_popup() -> None:
	"""Ends the popup created by a call to add_popup."""
	...

def end_tab() -> None:
	"""Ends the tab created by a call to add_tab."""
	...

def end_tab_bar() -> None:
	"""Ends the tab bar created by a call to add_tab_bar"""
	...

def end_tooltip() -> None:
	"""Ends the tooltip created by a call to add_tooltip."""
	...

def end_tree_node() -> None:
	"""Ends the tree node created by a call to add_tree_node."""
	...

def end_window() -> None:
	"""Ends the window created by a call to add_window."""
	...

def generate_stub_file(directory: str) -> None:
	"""Generates stub files."""
	...

def get_active_window() -> str:
	"""Returns the active window name."""
	...

def get_data(name: str) -> object:
	"""Retrieves data from storage."""
	...

def get_delta_time() -> float:
	"""Returns time since last frame."""
	...

def get_drawing_origin(name: str) -> (float, float):
	"""Returns the drawing origin."""
	...

def get_drawing_scale(name: str) -> (float, float):
	"""Returns the drawing scale."""
	...

def get_drawing_size(name: str) -> (float, float):
	"""Returns the size of a drawing widget."""
	...

def get_global_font_scale() -> float:
	"""Returns the global font scale."""
	...

def get_item_callback(item: str) -> str:
	"""Returns an item' callback"""
	...

def get_item_height(item: str) -> float:
	"""Returns an item's height."""
	...

def get_item_popup(item: str) -> str:
	"""Returns an item's popup."""
	...

def get_item_rect_max(item: str) -> [float, float]:
	"""Returns an item's maximum allowable size."""
	...

def get_item_rect_min(item: str) -> [float, float]:
	"""Returns an item's minimum allowable size."""
	...

def get_item_rect_size(item: str) -> [float, float]:
	"""Returns an item's current size."""
	...

def get_item_tip(item: str) -> str:
	"""Returns an item's tip."""
	...

def get_item_width(item: str) -> float:
	"""Returns an item's width."""
	...

def get_log_level() -> int:
	"""Returns the log level."""
	...

def get_main_window_size() -> [float, float]:
	"""Returns the size of the main window."""
	...

def get_marvel_version() -> str:
	"""Returns the current version of Marvel."""
	...

def get_mouse_drag_delta() -> (float, float):
	"""Returns the current mouse drag delta"""
	...

def get_mouse_pos(local: bool) -> (int, int):
	"""Returns the current mouse position in relation to the active window (minus titlebar) unless local flag is unset."""
	...

def get_plot_query_area(plot: str) -> List[float]:
	"""Clears a plot."""
	...

def get_style_item(item: int) -> (float, float):
	"""Returns a style item's value"""
	...

def get_table_item(table: str, row: int, column: int) -> str:
	"""Gets a table's cell value."""
	...

def get_table_selections(table: str) -> List[List[int]]:
	"""Retrieves data from storage."""
	...

def get_theme() -> str:
	"""Returns the current theme."""
	...

def get_theme_item(item: int) -> (float, float, float, float):
	"""Returns a theme item's color"""
	...

def get_thread_count() -> int:
	"""Returns the allowable thread count."""
	...

def get_threadpool_timeout() -> float:
	"""Returns the threadpool timeout in seconds."""
	...

def get_total_time() -> float:
	"""Returns total time since app started."""
	...

def get_value(name: str) -> Any:
	"""Returns an item's value or None if there is none."""
	...

def get_window_pos(window: str) -> List[float]:
	"""Gets a windows position"""
	...

def hide_item(name: str) -> None:
	"""Hides an item."""
	...

def insert_column(table: str, column_index: int, name: str, column: List[str]) -> None:
	"""Inserts a column into a table."""
	...

def insert_row(table: str, row_index: int, row: List[str]) -> None:
	"""Inserts a row into a table."""
	...

def is_item_activated(item: str) -> bool:
	"""Checks if an item has been activated."""
	...

def is_item_active(item: str) -> bool:
	"""Checks if an item is active."""
	...

def is_item_clicked(item: str) -> bool:
	"""Checks if an item is clicked."""
	...

def is_item_deactivated(item: str) -> bool:
	"""Checks if an item has been deactivated."""
	...

def is_item_deactivated_after_edit(item: str) -> bool:
	"""Checks if an item has been deactivated after editing."""
	...

def is_item_edited(item: str) -> bool:
	"""Checks if an item has been edited."""
	...

def is_item_focused(item: str) -> bool:
	"""Checks if an item is focused."""
	...

def is_item_hovered(item: str) -> bool:
	"""Checks if an item is hovered."""
	...

def is_item_toggled_open(item: str) -> bool:
	"""Checks if an item is toggled."""
	...

def is_item_visible(item: str) -> bool:
	"""Checks if an item is visible."""
	...

def is_key_down(key: int) -> bool:
	"""Checks if the key is down."""
	...

def is_key_pressed(key: int) -> bool:
	"""Checks if the key is pressed."""
	...

def is_key_released(key: int) -> bool:
	"""Checks if the key is released."""
	...

def is_mouse_button_clicked(button: int) -> bool:
	"""Checks if the mouse button is clicked."""
	...

def is_mouse_button_double_clicked(button: int) -> bool:
	"""Checks if the mouse button is double clicked."""
	...

def is_mouse_button_down(button: int) -> bool:
	"""Checks if the mouse button is pressed."""
	...

def is_mouse_button_dragging(button: int, threshold: float) -> bool:
	"""Checks if the mouse is dragging."""
	...

def is_mouse_button_released(button: int) -> bool:
	"""Checks if the mouse button is released."""
	...

def is_plot_queried(plot: str) -> bool:
	"""Clears a plot."""
	...

def is_threadpool_high_performance() -> bool:
	"""Checks if the threadpool is allowed to use the maximum number of threads."""
	...

def log(message: str, level: str) -> None:
	"""Logs a trace level log."""
	...

def log_debug(message: str) -> None:
	"""Logs a debug level log."""
	...

def log_error(message: str) -> None:
	"""Logs a error level log."""
	...

def log_info(message: str) -> None:
	"""Logs a info level log."""
	...

def log_warning(message: str) -> None:
	"""Logs a warning level log."""
	...

def move_item_down(item: str) -> None:
	"""Moves down up if possible and if it exists."""
	...

def move_item_up(item: str) -> None:
	"""Moves item up if possible and if it exists."""
	...

def open_file_dialog(extensions: List[str]) -> str:
	"""Opens an 'open file' dialog."""
	...

def run_async_function(name: str, data: object, return_handler: str) -> None:
	"""Runs a function asyncronously."""
	...

def run_file(name: str, file: str, flags: str) -> None:
	"""Runs a seperate Marvel app."""
	...

def save_file_dialog(extensions: List[str]) -> str:
	"""Opens an 'save file' dialog."""
	...

def select_directory_dialog() -> str:
	"""Opens a select directory dialog."""
	...

def set_color_map(plot: str, map: int) -> None:
	"""Sets the color map of the plot's series."""
	...

def set_drawing_origin(name: str, x: float, y: float) -> None:
	"""Sets the drawing origin (default is 0,0)."""
	...

def set_drawing_scale(name: str, x: float, y: float) -> None:
	"""Sets the drawing scale (default is (1,1))."""
	...

def set_drawing_size(name: str, width: int, height: int) -> None:
	"""Sets the size of a drawing widget."""
	...

def set_global_font_scale(scale: float) -> None:
	"""Changes the global font scale."""
	...

def set_item_callback(item: str, callback: str) -> None:
	"""Sets an item's callback if applicable."""
	...

def set_item_height(item: str, height: int) -> None:
	"""Sets an item's height if applicable."""
	...

def set_item_popup(item: str, popup: str) -> None:
	"""Sets an item's popup if applicable."""
	...

def set_item_tip(item: str, tip: str) -> None:
	"""Sets a simple tooltip for an item."""
	...

def set_item_width(item: str, width: int) -> None:
	"""Sets an item's width."""
	...

def set_key_down_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a key down event."""
	...

def set_key_press_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a key press event."""
	...

def set_key_release_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a key release event."""
	...

def set_log_level(level: int) -> None:
	"""Sets the log level."""
	...

def set_main_window_size(width: int, height: int) -> None:
	"""Sets the main window size."""
	...

def set_mouse_click_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a mouse click event."""
	...

def set_mouse_double_click_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a mouse double click event."""
	...

def set_mouse_down_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a mouse down event."""
	...

def set_mouse_drag_callback(callback: str, threshold: float, handler: str) -> None:
	"""Sets a callback for a mouse drag event."""
	...

def set_mouse_wheel_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a mouse wheel event."""
	...

def set_plot_xlimits(plot: str, xmin: float, xmax: float) -> None:
	"""Sets x axis limits of a plot. (can be undone with set_plot_xlimits_auto()"""
	...

def set_plot_xlimits_auto(plot: str) -> None:
	"""Sets plots x limits to be automatic."""
	...

def set_plot_ylimits(plot: str, ymin: float, ymax: float) -> None:
	"""Sets y axis limits of a plot. (can be undone with set_plot_ylimits_auto()"""
	...

def set_plot_ylimits_auto(plot: str) -> None:
	"""Sets plots y limits to be automatic."""
	...

def set_render_callback(callback: str, handler: str) -> None:
	"""Sets the callback to be ran every frame."""
	...

def set_resize_callback(callback: str, handler: str) -> None:
	"""Sets a callback for a window resizes."""
	...

def set_table_item(table: str, row: int, column: int, value: str) -> None:
	"""Sets a table's cell value."""
	...

def set_table_selection(table: str, row: int, column: int, value: bool) -> None:
	"""Sets a table's cell selection value."""
	...

def set_theme(theme: str) -> None:
	"""Set the application's theme to a built-in theme."""
	...

def set_thread_count(threads: int) -> None:
	"""Sets number of threads to use if the threadpool is active."""
	...

def set_threadpool_high_performance() -> None:
	"""Set the thread count to the maximum number of threads on your computer."""
	...

def set_threadpool_timeout(time: float) -> None:
	"""Sets the threadpool timeout."""
	...

def set_value(name: str, value: object) -> None:
	"""Sets an item's value if applicable."""
	...

def set_window_pos(window: str, x: float, y: float) -> None:
	"""Sets a windows position"""
	...

def show_about() -> None:
	"""Shows the about window."""
	...

def show_debug() -> None:
	"""Shows the debug window."""
	...

def show_documentation() -> None:
	"""Shows the documentation window."""
	...

def show_item(name: str) -> None:
	"""Shows an item if it was hidden."""
	...

def show_logger() -> None:
	"""Shows the logging window."""
	...

def show_metrics() -> None:
	"""Shows the metrics window."""
	...

def show_source() -> None:
	"""Shows the source code for the current app."""
	...

def unindent(name: str, offset: float, parent: str, before: str) -> None:
	"""Unindents following items."""
	...

