# Basic details
create_enterprise_title = "//h5[text() = 'Create Enterprise']"
trade_name_field = "//input[@name = 'tradeName']"
legal_name_field = "//input[@name = 'legalName']"
website_field = "//input[@name = 'website']"
enterprise_email_field = "//input[@placeholder='Enter email address']"
pan_field = "//input[@name = 'pan']"
cin_field = "//input[@name = 'cin']"
ba_code_field = "//input[@name = 'baCode']"
timezone_dropdown = "//select[@id= 'timezone']"

# Registered Address
registered_address_field = "//input[@name= 'registeredAddress.address']"
registered_pin_code_filed = "(//input[@placeholder= 'Enter Pincode' and @id ='myInput'])[1]"
registered_contact_number_field = "(//input[@placeholder= 'Enter contact number' ])[1]"

# Corporate Address
corporate_address_field = "//input[@name= 'corporateAddress.address']"
corporate_pin_code_filed = "(//input[@placeholder= 'Enter Pincode' and @id ='myInput'])[2]"
corporate_contact_number_field = "(//input[@placeholder= 'Enter contact number' ])[2]"
same_registered_address_check_box = "//input[@type = 'checkbox' and @name = 'registeredaddress']"

# Buttons
next_step_button = "//div[@class='d-flex justify-content-center align-items-center text-14 p-2rx headerBar ml-1 next-button enabledButton']"
discard_button = "//div[@class='px-1 d-flex justify-content-center align-items-center blue-60 p-2rx cursor-pointer']"

#erro messages
website_field_error_message="//span[@class='error' and contains(text(),'Website must be a URL address')]"
cin_field_error_message="//span[@class='error' and contains(text(),'Please enter a valid CIN')]"
existing_cin_error_message="//span[@class='error' and contains(text(),'Cin already exists.')]"
pincode_error_popup="(//div[@role='alert'])[1]"
city_field_disabled="//select[@id='corporateAddress.city']"
state_field_disabled= "//select[@id='corporateAddress.state']"
country_field_disabled="//select[@id='corporateAddress.country']"
corporate_address_field_disabled="(//input[@name='registeredAddress.address' and @class='input'])[2]"
corporate_pin_code_filed_disabled="(//input[@placeholder= 'Enter Pincode' and @id ='myInput'])[2]"
corporate_contact_number_field_disabled = "(//input[@placeholder= 'Enter contact number' ])[2]"

timezone_dropdown_option="//select[@placeholder='Select timezone']//option[contains(text(),'Africa/Abidjan (UTC)')]"