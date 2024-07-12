# Enterprise Information
# Basic Details
# here I am going to add prefix "summary" to "field"
trade_name_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][1]/span[@class ='text-13']"
legal_name_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][2]/span[@class ='text-13']"
website_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][3]/span[@class ='text-13']"
email_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][4]/span[@class ='text-13']"
pan_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][5]/span[@class ='text-13']"
cin_summary_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][1]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][6]/span[@class ='text-13']"
ba_code_summary_field =  "//input[@name='baCode']"

# Registered Address
address_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-12 detail-display'][1]/span[@class ='text-13']"
city_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][2]/span[@class ='text-13']"
pincode_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][1]/span[@class ='text-13']"
state_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][3]/span[@class ='text-13']"
country_field = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][4]/span[@class ='text-13']"
contact_number = "//div[@class= 'd-flex flex-column py-4 px-2r'][2]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][5]/span[@class ='text-13']"


# Corporate Address
corp_contact_number = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][5]/span[@class ='text-13']"
corp_pincode = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][1]/span[@class ='text-13']"
corp_city = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][2]/span[@class ='text-13']"
corp_state = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][3]/span[@class ='text-13']"
corp_country = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-6 detail-display'][4]/span[@class ='text-13']"
corp_address = "//div[@class= 'd-flex flex-column py-4 px-2r'][3]/descendant::div[@class= 'd-flex flex-column col-12 detail-display'][1]/span[@class ='text-13']"


# Nav Option Buttons
enterprise_information_nav_button = "//label [@class= 'd-flex pl-4 justify-content-start align-items-center summaryType cursor-pointer' and text() = ' Enterprise Information ']"
application_access_nav_button = "//label [@class= 'd-flex pl-4 justify-content-start align-items-center summaryType cursor-pointer' ][contains(text(),' Application Access ')]"
primary_users_nav_button = "//label [@class= 'd-flex pl-4 justify-content-start align-items-center summaryType cursor-pointer' and text() = ' Primary Users ']"
audit_logs_nav_button = "//label [@class= 'd-flex pl-4 justify-content-start align-items-center summaryType cursor-pointer' and text() = ' Audit Logs ']"


# Application Instances
add_instance_button = "//div[@class = 'd-flex justify-content-between align-items-center text-14 headerBar p-1r enabledButton cursor-pointer']"
# Primary User
add_user_button = "//div[@class= 'd-flex justify-content-between align-items-center text-14 headerBar p-1r enabledButton cursor-pointer']"
# primary_user_name = "//div[@col-id='name']/descendant::div[@class='d-flex']"
primary_name = "//div[@col-id='name']/descendant::div[@class='d-flex']"
primary_user_email = "//div[@class = 'ag-center-cols-container' ]/descendant::div[@col-id='email']"
primary_username = "//div[@class = 'ag-center-cols-container' ]/descendant::div[@col-id='username']"
primary_user_role = "//div[@class = 'ag-center-cols-container' ]/descendant::div[@col-id='role']"
primary_user_date = "//div[@class = 'ag-center-cols-container' ]/descendant::div[@col-id='date']"


# Enterprise Summary Page
options_menu = "//span[@class='text-13 blue-60']"
list_elements = "//button[contains(@class,'dropdown-item text-13 p-dropdown-menu-items')]"
list_contains_element = "//button[contains(text(),'Edit Enterprise')]"
list_is_visible = "//ul[@class='dropdown-menu grey-70 show']"
save_edit = "//span[@class='px-1']"
activate_enterprise_option_status = "//button[@class='dropdown-item text-13 p-dropdown-menu-items border-bottom-grey20']"
activate_enterprise_option = "//button[contains(text(),'Activate Enterprise')]"
deactivate_enterprise_option = "//button[contains(text(),'Deactivate Enterprise')]"
activate_enterprise_button = "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder' and text()='Activate']"
deactivate_enterprise_button = "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder' and text()='Deactivate']"
back_to_all_enterprise_page = "//span[@class='text-11 blue-60 cursor-pointer d-flex align-items-center']"


# Edit Enterprise Page
Legal_name = "//input[@placeholder='Enter legal name']"


#Enterprise Summary page > Application Access option
select_instance = "//label[contains(text(),'Instance')]"
select_app = "//select[@id='application']"
zwing_staging = "//input[@id='01HQ0K170A85S4HDFXKRKD2F6N']"
zwingers = "//input[@id='01HQ0K1704ATB914AAC9XSX8AN']"
easymygst_production = "//input[@id='01HQ0K170E23E1XQ13SNSMFDN0']"
ginesys_staging = "//input[@id='01HQ0K170JGK94YDEADA2XS2YM']"
browntape_production = "//input[@id='01HQ0K170NNW7CBFABTDBTVKM6']"
browntape_demo = "//input[@id='01HQ0K170SKG88KQF596MFTT21']"
browntape_staging = "//input[@id='01HQ0K170XCWCAV1AVW8MAHCE3']"
save_instance = "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder']"
manual_add_instance = "//input[@id='add-new-instance']"
label_instance_name = "//label[contains(text(),'Instance Name')]"
name_of_instance = "//input[@placeholder='Enter name for the new instance']"
instance_type = "//select[@id='env']"
instance_url = "//input[@name='host']"
reference_id = "//input[@name='refId']"


select_instance_list = "//label[@class='mr-2 text-13']"
select_instance_url ="//label[@class='mr-2 text-13']//following::label"
select_instance_lastupdate_date ="//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height'and@col-id='lastUpdatedAt']"
application_instance_list = "//div[@class='ag-body-viewport ag-layout-normal ag-row-no-animation']"
delete_list_option = "//div[@class='d-flex justify-content-center align-items-center h-100']//following::img[@name='deleteInstance']"
remove_instance_button = "//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder w-10r']//following:: span"

redirect_url = "//input[@name='redirectUrl']"
primary_user_row1= "//div[@class='ag-center-cols-viewport']"
edit_enterprise_option= "//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),'Edit Enterprise')]"
edit_enterprise_trade_name= "//input[@name='tradeName']"
edit_enterprise_save_button= "//span[@class='px-1']"

dashbord_list_legal_name="(//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height'])[2]"
dashboard_list_trade_name="(//div[@class='ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height'])[1]"

application_instances_row_1 = "//div[@class='ag-body-viewport ag-layout-normal ag-row-no-animation']//descendant::div[@aria-colindex='1']"
instance_details_application_name = "(//span[@class='text-11 grey-60']//following-sibling::span)[1]"
instance_details_env_name = "(//span[@class='text-11 grey-60']//following-sibling::span)[2]"
instance_details_url = "(//span[@class='text-11 grey-60']//following-sibling::span)[5]"
element_in_application_column = "(//div[@class='d-flex align align-items-center']//span)"

application_access_header_field = "//span[@class='text-20 py-2' and text()='Application Instances']"
primary_users_header_field = "//span[@class='text-20 py-2' and text()='Primary Users']"
audit_logs_header_field = "//span[@class='text-20 py-2' and text()='Audit Logs']"
enterprise_information_header_field = "//span[@class='text-20 py-2' and text()='Basic Details']"
enterprise_icon="//img[@src='/Images/enterprise.svg']"

remove_instance_header = "//span[@class='text-20' and text()='Remove Instance']"
remove_instance_icon_row_1 = "//div[@class='d-flex justify-content-center align-items-center h-100']/img[@name='deleteInstance']"
instance_summary_header_field = "//h5[@class='m-0' and text()='Instance Summary']"
add_user_option = "//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),'Add User')]"
application_instance_option_dropdown = "//ul[@class='dropdown-menu grey-70 show']"
application_instance_option_button = "//span[@class='text-13 blue-60']"

verify_email="//span[@class='error' and text()='Email must be an email']"
verify_phone_number="//input[@class='input' and @placeholder='Enter phone number']"
attach_button_config="//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder m-0']"
save_config_instance_button = "(//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder m-0'])[1]"

eye_fabric_icon = "//div[@class='d-flex justify-content-center align-items-center h-100']//img[1]"
remove_instance_icon="//div[@class='d-flex justify-content-center align-items-center h-100']//child::img"

application_instance_configuration = "//div[@class='d-flex px-4 border-bottom-grey20']//span[contains(text(),'Configuration')]"
application_instance_history = "//div[@class='d-flex px-4 border-bottom-grey20']//span[contains(text(),'History')]"
div_element_in_app_instance_table = "//div[@role='gridcell']"
service_name ="(//h5[contains(text(),'Addon Service')]//following::span[contains(text(),'Ginesys-POS')])[1]"
edit_instance_icon = "(//div[@class='d-flex justify-content-center align-items-center h-100']//img[2])"
service_1_chechbox = "//div[@class='bg-white sidebar position-fixed h-100 sidebar-transition w-50']//input[@class='checkbox-2 m-2']"
select_service_end_date = "//div[@class='bg-white sidebar position-fixed h-100 sidebar-transition w-50']//h5[text()='Primary Service']//ancestor::div[@class='d-flex flex-column w-full m-0']//input[@placeholder='Select end date']"
buffer_period_field = "//div[@class='bg-white sidebar position-fixed h-100 sidebar-transition w-50']//h5[text()='Primary Service']//ancestor::div[@class='d-flex flex-column w-full m-0']//label[contains(text(),'Buffer Period (in days)')]//following::input[1]"
update_instance = "//div[@class='bg-white sidebar position-fixed h-100 sidebar-transition w-50']//ancestor::button"
inavlid_pan_error="//span[@class='error' and contains(text(),'Please enter a valid PAN')]"
existing_pan_error="//span[@class='error' and contains(text(),'Pan already exists')]"

enterprise_information_icon1= "//div[@class='bg-yellow pill d-flex justify-content-center align-items-center mr-12']"
primary_user_icon2="//div[@class='bg-grey-10 pill d-flex justify-content-center align-items-center mr-12']//span[contains(text(),'2')]"
application_user_icon3="//div[@class='bg-grey-10 pill d-flex justify-content-center align-items-center mr-12']//span[contains(text(),'3')]"
element_in_history_timestamp = "//div[@col-id='changedAt']"

# Buttons
next_step_button = "//div[@class='d-flex justify-content-center align-items-center text-14 p-2rx headerBar ml-1 next-button enabledButton']"
discard_button = "//div[@class='px-1 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer']"
next_step_disable_button="//div[@class='d-flex justify-content-center align-items-center text-14 p-2rx headerBar ml-1 next-button pe-none grey-30']"

application_instance_text="//span[@class='text-20 py-2' and contains(text(),'Application Instances')]"
cancel_instance="//div[@class='p-3 margin-secondary text-14 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder']"

zwing_app_option= "//select[@id='application']//option[@value='1']"
easemygst_app_option="//select[@id='application']//option[@value='2']"
ginesyserp_app_option="//select[@id='application']//option[@value='3']"
browntape_app_option="//select[@id='application']//option[@value='4']"
crm_app_option="//select[@id='application']//option[@value='5']"
select_instance_text="//span[@class='text-11 grey-60 m-12 delayed-display']"

enterprise_field_add_instance="//select[@name='enterprise']"
discard_button_add_user = "//div[@class='px-1 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer']"
discard_changes_popup_window="//span[@class='text-20']"
discard_button_discard_change_popup_window="//button[@class='submitbtn confirmButton text-14 submitbtnEnabled font-weight-bolder']"
cancel_button_discard_change_popup_window="//div[@class='p-3 margin-secondary text-14 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer font-weight-bolder']"
add_primary_user_text_enterprise_summary="//div//h5[@class='m-0' and contains(text(),'Add Primary User')]"
add_instance_text = "//span[@class='text-20' and contains(text(),'Add Instance')]"

option_add_user = "//button[@class='dropdown-item text-13 p-dropdown-menu-items' and contains(text(),'Add User')]"


edit_enterprise_legal_name= "//input[@name='legalName']"
edit_enterprise_website="//input[@name='website']"
edit_enterprise_email = "//input[@name='email']"
edit_enterprise_pan="//input[@name='pan']"
edit_enterprise_cin="//input[@name='cin']"
edit_enterprise_bacode="//input[@name='baCode']"
edit_enterprise_registered_address="(//input[@name='registeredAddress.address'])[1]"
edit_enterprise_pincode="(//input[@name='registeredAddress.pincode'])[1]"
edit_enterprise_contact_no="(//input[@name='registeredAddress.contactNumber'])[1]"

disable_save_button= "//div[@class='d-flex justify-content-center align-items-center text-14 p-2rx headerBar ml-1 next-button next-button pe-none grey-30']"
next_page_element = '//div[@ref="btNext"]'
status_column = '//div[@col-id="status" and @role="gridcell"]/span'
total_pages = '//span[@ref="lbTotal"]'
total_rows = '//span[@ref="lbLastRowOnPage"]'


audit_data_div = "//div[@class='ag-body-viewport ag-layout-normal ag-row-no-animation']"
corporate_address_checkbox = "//input[@type='checkbox']"
corporate_address ="(//input[@name='registeredAddress.address'])[2]"
audit_logs_enterprise_summary= "//span[@class='text-20 py-2']"

element_in_existing_user_search_dropdown = "//div[@class='w-max d-flex flex-column col-12 search-fields position-absolute']"
search_existing_user = "//input[@placeholder='Type in a name to search']"
validation_popup = "//div[@class='Vue-Toastification__toast Vue-Toastification__toast--warning top-right']//div[text()='User already exists in the enterprise']"
red_cross_logo = "//img[@src='/Images/red-cross.svg']"
back_to_all_users_page = "//span[@class='text-11 blue-60 cursor-pointer d-flex align-items-center' and contains(text(),'All Users')]"

from_date = "//div[@class='dp__cell_inner dp__pointer dp__range_between' and text()='date']"
to_date ='//div[@class="dp__cell_inner dp__pointer dp__today dp__date_hover_end" and text()="dateago"]'