users_icon ="//img[@class='icon' and @src='/Images/user.svg']"

#sort records
sort_by_latest_first = "//span[ @class='text-12 grey-60' and  contains(text(),'Sort by Latest First')]"
sort_filter_list_option = "//div[@data-bs-toggle='dropdown']"
latest_first = "//button[@class='dropdown-item grey-100 text-14' and contains(text(),'Latest First')]"
oldest_first = "//button[@class='dropdown-item grey-100 text-14' and contains(text(),'Oldest First')]"
name_ascending_button = "//button[@class='dropdown-item grey-100 text-14' and contains(text(),'Name Ascending')]"
name_descending_button ="//button[@class='dropdown-item grey-100 text-14' and contains(text(),'Name Descending')]"
drop_down_list = "//ul[@class='dropdown-menu show']"
date = "//div[@col-id='date']"
date_element_in_row = "(//div[@role='gridcell' and @col-id='date'])"
name_column = "//div[@col-id='name']"
name_list_after_ascending_sort = "//div[contains(@class,'ag-row-no-focus')]/div/span/div/div[2]"
name_list_after_descending_sort = "//div[contains(@class,'ag-row-no-focus')]/div/span/div/div[2]"
sort_button_after_ascending_sort = "//div[@id='dropdownmenu']/span[text()='Sort by Name Ascending']"
sort_button_after_descending_sort = "//div[@id='dropdownmenu']/span[text()='Sort by Name Descending']"
clear_sort_filter = "//img[@class='sort ml-2']"
name_element_in_row = '//div[@col-id="name" and @role="gridcell"]//span'


#search bar for users
user_search_field = "//input[@placeholder='Search Users']"

#filter records
filter_by_enterprise = "//span[@class='text-12 grey-60'and contains(text(),'Filter by Enterprise')]"
enterprise_search = "//input[@class='search-enterprise']"
enterprise_search_checkbox = "//button[@class='dropdown-item grey-100 text-14 d-flex align-items-center p-0']"
total_record_count = "//span[@ref='lbRecordCount']"
record_count_on_page = "//span[@ref='lbLastRowOnPage']"
enterprise_element_in_enterprise_column = "//div[@col-id='enterprise']//div[@class='d-flex align-items-center']"
enterprise_field_on_user_summary_page = "//span[text()='Enterprises']//following-sibling::span"

user_row_1 = "//div[@class='ag-center-cols-container']//child::div[@row-index='0']"
user_row_9 = "//div[@class='ag-center-cols-container']//child::div[@row-index='8']"

#select enterprise
select_enterprise = "//span[@class='text-13 blue-60' and contains(text(),'Select Enterprise')]"
filter_enterprise_dropdown_element = "//div[@class='dropdown-menu show']//descendant::label"
first_enterprise = "//div[@class= 'dropdown-menu show']/child::ul/li"

#options
select_options="//span[@class='text-13 blue-60' and contains(text(),'Options')]"

#edit user
edit_user="//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),' Edit User ')]"
edit_user_first_name= "//input[@class='input' and @placeholder='Enter first name']"
edit_user_last_name ="//input[@class='input' and @placeholder='Enter last name']"
edit_user_phone_number="//input[@class='input' and @placeholder='Enter phone number']"
edit_user_email="//input[@class='input' and @placeholder='Enter email']"
edit_user_username="//input[@class='input' and @placeholder='Enter username']"
update_user_button="//div[@class='d-flex']//child::button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder']"
disabled_update_user_button = "//button[@class= 'submitbtn confirmButton text-14 submitbtnDisabled font-weight-bolder']"
cancel_edit_user_button="//div[@class='p-3 margin-secondary text-14 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder' ]"

#deactivate user
deactivate_user="//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20' and contains(text(),'Deactivate User')]"
deactivate_button="//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder']"
cancel_deactivate_button="//div[@class='p-3 margin-secondary text-14 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder']"
activate_user = "//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20' and contains(text(),'Activate User')]"
deactivate_or_activate_option="//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20']"
activate_button = "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder']"

activate_enterprise="//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20' and contains(text(),'Activate Enterprise')]"
deactivate_enterprise="//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20' and contains(text(),'Deactivate Enterprise')]"

#add app instances
add_app_instance="//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),' Add App Instance ')]"
#Attach Instance
enterprise_dropdown= "//select[@id='enterprise' and @class='input select-custom']"
enterprise_dropdown_option="//select[@id='enterprise' and @class='input select-custom']/option[@value='1']"
select_app="//select[@id='application' and @class='input select-custom']"

first_instance = '(//input[@name="instanceSelection"])[1]'
save_instance_button="//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder' ]"
cancel_button="//div[@class='p-3 margin-secondary text-14 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder']"

#Application access section
select_application_access="//label[@class='d-flex pl-4 justify-content-start align-items-center summaryType cursor-pointer' and contains(text(),'Application Access')]"
instance_list_select_enterprise= "//div[@class='ag-body ag-layout-normal']"
attach_instance= "//div[@class='d-flex justify-content-between align-items-center text-14 headerBar p-1r enabledButton cursor-pointer']"
remove_instance_icon= "//div[@class='d-flex justify-content-center align-items-center h-100']"
attach_instance_window= "//div[@class='d-flex align-items-center mb-2']"
remove_instance_button= "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder w-10r']"


#user_summary
# element_should_contain_name = "//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13' and contains(text(),'${info_dict.Name}')]"
# element_should_contain_lastname="//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13' and contains(text(),'${info_dict.Last_Name}')]"
# element_should_contain_phone_number="//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13' and contains(text(),'${info_dict.Phone_Number}')]"
# element_should_contain_email="//span[@class='text-11 grey-60']/following-sibling::span[@class='text-13' and contains(text(),'${info_dict.U_email}')]"
# element_should_contain_username="//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13' and contains(text(),'${info_dict.Username}')]"


# Rest Password
reset_password_button = "//button[@class = 'dropdown-item text-13 p-dropdown-menu-items' and text()=' Reset Password ']"
reset_autogenerted_pw_button = '//button[@class="submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder rounded p-0 w-8r"]'
auto_generate_password_checkbox = "(//div[@class='w-max d-flex pr-1 p-checkbox']//child::input)[1]"
require_password_checkbox = "(//div[@class='w-max d-flex pr-1 p-checkbox']//child::input)[2]"
reset_password_popup_button = "//button[@class= 'submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder rounded p-0 w-8r']"
cancel_rest_password_button = "//div[@class = 'p-3 margin-secondary text-14 d-flex justify-c    ontent-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder']"
reset_password_field = "//input[@placeholder = 'Enter password']"
reset_confirm_password_field = "//input[@placeholder = 'Enter confirm password']"
something_went_wrong_alert = "//div[@class = 'Vue-Toastification__toast-body' and text() = 'Something went wrong.']"
password_policy_error = "//span[@title = 'PasswordPolicy Error']"
password_match_cross_label = "//div[@class = 'd-flex align-items-center text-danger' and text()= ' Passwords match ']"
successful_pw_reset = '//div[@role="alert" and text()="Reset Password successfully"]'
forget_password_window_text="//h1[@id='kc-page-title' and text()='Forgot your password?']"
forget_password_window_email="//div[@class='d-flex flex-column']//input[@id='email' and @class='input-email']"
forget_password_window_reset_button="//button[@class='submitbtn submitbtnEnabled']//span[text()='Reset Password']"




# Basic Detail
user_first_name = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[1]"
user_last_name = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[2]"
users_phone_number = '//span[text()="Phone number"]//following-sibling::span'
user_phone_number = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[3]"
user_email = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[4]"
user_enterprise_name = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[5]"
user_username = "(//div[@class='d-flex flex-column col-6 detail-display']//child::span[@class='text-13'])[6]"
user_role = "//div[@class='d-flex flex-column col-6 detail-display']//span[text()='Role']//following-sibling::span"
# get details of legal name locator
legal_name_of_user= "//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height']/div[@class='d-flex align-items-center']"
select_enterprise_dropdown_elements = "(//div[@class='dropdown-menu show']//descendant::label)"

#User row 1 locators on users page
user_name_row_1 = "//div[@row-index='0']//div[@col-id='name']//div//div[2]"
email_row_1 = "//div[@row-index='0']//div[@col-id='email']"
enterprise_row_1 = "//div[@row-index='0']//div[@col-id='enterprise']"
date_row_1 = "//div[@row-index='0']//div[@col-id='date']"

#reset password window
name_on_rp_window = "//div[@class='d-flex flex-column my-3']//span[contains(text(),'Name')]"
email_on_rp_window = "//div[@class='d-flex flex-column my-3']//span[contains(text(),'Email')]"
enterprise_on_rp_window = "//div[@class='d-flex flex-column my-3']//span[contains(text(),'Enterprise')]"

#mrunal's locators
user_name_table="//div[@class='ag-body-viewport ag-layout-normal ag-row-no-animation']//div[@col-id='name']/span/div/div[2]"
Table_locator="//div[@class='ag-center-cols-container']"
search_result_name="(//div[@class='d-flex align-items-center'])[1]"
filter_dropdown = "//div[@class='dropdown-menu show']"
selected_enterprise_name= "//div[@class='d-flex align-items-center grey-60 p-8x sortbutton py-2 px-3 mr-3']//span[@class='text-13 blue-60']"
option_dropdown= "//ul[@class='dropdown-menu grey-70 show']"
enterprise_dropdown_first_option = "(//div[@class='dropdown-menu show']/ul)[1]"

checkbox_selected_count ="//span[@class='text-12' and contains(text(),'+4')]"
user_count = '//span[@ref="lbRecordCount"]'

select_app_dropdown= "(//select[@id='application']//option)[2]"
attach_window_extended= "//div[@class='d-flex flex-column m-12 fade-in-delayed h-8r']"
select_instance= "//input[@type='checkbox']"
#alert
cannot_post_alert = "//div[@role='alert' and contains(., 'Cannot POST')]"

first_row_enterprise= "//div[@class='ag-row-even ag-row-no-focus ag-row-not-inline-editing ag-row ag-row-level-0 ag-row-position-absolute ag-row-first'][1]"

edit_enterprise_option = "//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),'Edit Enterprise')]"
edit_enterprise_trade_name = "//input[@name='tradeName']"
edit_enterprise_save_button = "//span[@class='px-1']"
reset_password_popup= "//div[@class='Vue-Toastification__toast-body']"

total_page_count = '//span[@ref="lbRecordCount"]'
page_count = '//span[@ref="lbTotal"]'
next_page = '//span[@class="ag-icon ag-icon-next"]'

attach_app_instance = "//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),' Attach App Instance ')]"     # change

