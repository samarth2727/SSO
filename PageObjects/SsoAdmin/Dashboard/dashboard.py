ginesys_logo = "//div[@class ='iconLogo']"
enterprises_header = "//div[@class = 'd-flex justify-content-between align-items-center headerBar']/span[text()='Enterprises']"
add_new_enterprise_button = "//span[@class= 'px-1']"
enterprises_added_label = "(//span[@class = 'text-14' and text() = 'Enterprise Added']/following-sibling::span[@class = 'text-24'])[1]"
active_enterprises_label = "(//span[@class = 'text-14' and text() = 'Active Enterprises']/following-sibling::span[@class = 'text-24'])[1]"
active_app_instances = "(//span[@class = 'text-14' and text() = 'Active App Instances']/following-sibling::span[@class = 'text-24'])[1]"
trader_name_search_result = "//div[@class= 'ag-row-even ag-row-no-focus ag-row-not-inline-editing ag-row ag-row-level-0 ag-row-position-absolute ag-row-first ag-row-last']/div[@col-id='tradeName']"
search_field = "//input[@placeholder='Search Enterprises']"
dashboard_icon = '//img[@src="/Images/enterprise.svg"]'
first_search_result = "//div[@class= 'ag-row-even ag-row-no-focus ag-row-not-inline-editing ag-row ag-row-level-0 ag-row-position-absolute ag-row-first ag-row-last']/div[@col-id='tradeName']"
search_result_users_count = "//div[@class= 'ag-row-even ag-row-no-focus ag-row-not-inline-editing ag-row ag-row-level-0 ag-row-position-absolute ag-row-first ag-row-last']/div[@col-id='users']"
enterprise_status_on_dashboard = "//div[@col-id='status']/span"

# search enterprises
search_enterprises = "//div[@class='ag-center-cols-viewport']"

search_result = "//div[@class='ag-center-cols-viewport']//following::div[@col-id='tradeName']//span[text()='enterprise_name']"

basic_details_enterprise_summary = "//span[@class='text-20 py-2' and contains(text(),'Basic Details')]"
edit_enterprise_enterprise_summmary = "//div//h5[@class='m-0' and contains(text(),'Edit Enterprise')]"

trade_name_filter= "(//span[@class='ag-icon ag-icon-menu'])[1]"

filter_pincode= "(//span[@ref='eName'])[1]"
filter_autosize_this_column = "(//span[@ref='eName'])[2]"
filter_autosize_all_column = "(//span[@ref='eName'])[3]"
filter_reset_columns = "(//span[@ref='eName'])[4]"
pincolumn_no_pin = "//span[@class='ag-menu-option-part ag-menu-option-text' and contains(text(),'No Pin')]"
pincolumn_pin_left = "//span[@class='ag-menu-option-part ag-menu-option-text' and contains(text(),'Pin Left')]"
pincolumn_pin_right = "//span[@class='ag-menu-option-part ag-menu-option-text' and contains(text(),'Pin Right')]"

trade_name_column_before_shift = "(//span[@ref='eText'])[1]"
trade_name_column_after_shift = "(//span[@ref='eText' ])[7]"

legal_name_filter = "(//span[@class='ag-icon ag-icon-menu'])[2]"
legal_name_column_before_shift = "(//span[@class='ag-header-cell-text'])[2]"
legal_name_column_after_shift = "(//span[@class='ag-header-cell-text'])[1]"
search_result_enterprise_trade_name= "(//div[@col-id='tradeName'])[2]"

empty_div_table = "(//div[@class='ag-body-viewport ag-layout-normal ag-row-no-animation'])"

enterprise_field_calendar= "//input[@class='dp__pointer dp__input_readonly dp__input dp__input_icon_pad dp__input_reg']"
calendar_dropdown= "//div[@class='dp__menu_inner']"

date_10_april = "//div[@class='dp__cell_inner dp__pointer dp__range_between' and text()='10']"
date_15_april ="//div[@class='dp__cell_inner dp__pointer dp__date_hover_end' and text()='12']"

select_date = "//button[@class='dp__action_button dp__action_select' and contains(text(),'Select')]"

total_record_count = "//span[@ref='lbRecordCount']"
overview ="//span[@class='text-20' and contains(text(),'Overview')]"
overview_collapse="//button[@class='accordion-button collapsed']"
overview_verify="//button[@class='accordion-button']"
ginesys_one_apps="//span[@class='text-16 font-weight-600' and text()='Ginesys One Apps']"
first_record_enterprise="(//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height'])[1]"
column_names_checkbox="//span[@class='ag-tab']"
filter_by_column_name_search="//input[@class='ag-input-field-input ag-text-field-input']"
trade_name_column ="//span[@class='ag-header-cell-text' and  contains(text(),'Trade Name')]"
trade_name_checkbox="//span[@class='ag-column-select-column-label' and contains(text(),'Trade Name')]"
all_column_name_checkboxes="//div[@class='ag-column-select-header-checkbox ag-labeled ag-label-align-right ag-checkbox ag-input-field']"
legal_name_checkbox="//span[@class='ag-column-select-column-label' and contains(text(),'Legal Name')]"
legal_name_column="//span[@class='ag-header-cell-text' and  contains(text(),'Legal Name')]"
date_enterprise_added="(//span[@class = 'text-14' and text() = 'Enterprise Added']/following-sibling::span[@class = 'text-24'])[2]"
date_enterprise_activated="(//span[@class = 'text-14' and text() = 'Enterprises Activated']/following-sibling::span[@class = 'text-24'])[1]"
date_enterprise_deactivated="(//span[@class = 'text-14' sand text() = 'Enterprises Deactivated']/following-sibling::span[@class = 'text-24'])[1]"

cross_icon_calendar="(//*[name()='svg'][@class='dp__icon dp__clear_icon dp__input_icons'])[1]"
search_result_first_row= "//div[@class='asg-full-width-container']"