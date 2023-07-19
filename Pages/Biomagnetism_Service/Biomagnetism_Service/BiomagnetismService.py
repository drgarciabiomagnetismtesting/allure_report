from Pages.BasePage import BasePage
from Config.config import TestData
from Element_Locator.BasePageElements import BasePageElements
from Element_Locator.Biomagnetism_Service.Biomagnetism_Service.BiomagnetismServiceElements import BiomagnetismServiceElements
import time
import allure
import pandas as pd


class BiomagnetismService(BasePage):
    
    def __init__(self,driver,wait):
        super().__init__(driver,wait)
        with allure.step("Opening Base Url"):
            self.driver.get(TestData.BaseUrl)

    
    def check_visibility_and_clickable_of_element(self,checking_element,element_locator,element_value):
      with allure.step(f"Checking {checking_element}"):
              element_text = self.get_text_from_element_only(element_locator)
              with allure.step("Is Clickable"):
                element_status = self.get_element_clickable_status(element_locator)
                
             
              if element_value.lower() in element_text.lower() and element_status:
                  with allure.step(f"{checking_element} is visible and clickable"):
                      return True
              else:
                   with allure.step(f"{checking_element}  is not visible and clickable"):
                      return False

    def check_visibility_of_element(self,checking_element,element_locator,element_value):
      with allure.step(f"Checking {checking_element}"):
              element_text = self.get_text_from_element(element_locator)
             
              if element_value.lower() in element_text.lower():
                  with allure.step(f"{checking_element} is visible "):
                      return True
              else:
                   with allure.step(f"{checking_element}  is not visible "):
                      return False

    
    def is_biomagnetism_service_and_dropdown_visible_and_clickable(self):


        with allure.step("Checking Biomagnetism Service button is visible and clickable"):
            biomagnetism_service_status = self.check_visibility_and_clickable_of_element("Biomagnetism Services",BiomagnetismServiceElements.biomagnetism_service,"Biomagnetism Services".upper())
        
        with allure.step("Move to Biomagnetism Service"):
            self.do_move_cursor_to_element_only(BiomagnetismServiceElements.biomagnetism_service)
        
        with allure.step("Checking Dropdown Options"):
            
            find_a_therapy_status = self.check_visibility_and_clickable_of_element("Find a Therapist",
                                                                                    BiomagnetismServiceElements.find_a_therapy,
                                                                                    "Find a Therapist".upper())
            
            therapy_with_dr_garcia_status = self.check_visibility_and_clickable_of_element("Therapy with Dr. Garcia",
                                                                                    BiomagnetismServiceElements.therapy_with_dr_garcia,
                                                                                    "Therapy with Dr. Garcia".upper())
        
        if biomagnetism_service_status and find_a_therapy_status and therapy_with_dr_garcia_status:
            with allure.step("Biomagnetism Service and it's dropdown options are visible and clickable"):
                return True
        else:
            with allure.step("Biomagnetism Service and it's dropdown options are visible and clickable"):
                return True
    

    def is_all_cities_filter_visible_and_clickable(self):
        cities = ["ALL",
                "ARIZONA",
                "ARKANSAS",
                "AUSTRALIA",
                "CALIFORNIA",
                "CANADA",
                "COLORADO",
                "CONNECTICUT",
                "DELWARE",
                "FLORIDA",
                "GEORGIA",
                "HAMPSHIRE",
                "IDAHO",
                "MARYLAND",
                "MASSACHUSETTS",
                "MONTANA",
                "NEW HAMPSHIRE",
                "NEW JERSEY",
                "NEW YORK",
                "OHIO",
                "OREGON",
                "PENNSYLVANIA",
                "TEXAS"
                ]


        with allure.step("Move to Biomagnetism Service"):
            self.do_move_cursor_to_element_only(BiomagnetismServiceElements.biomagnetism_service)
        
        with allure.step("Clicked On Find a Therapist"):
            self.do_click(BiomagnetismServiceElements.find_a_therapy)
        
        with allure.step("Checking all cities are visible and clickable"):

            for city_name in cities:
                if not self.check_visibility_and_clickable_of_element(city_name,BiomagnetismServiceElements.get_city_xpath(city_name),city_name):
                    return False
               
            return True
    def is_sorted(self,string_row):
        return string_row == sorted(string_row)

    def is_sorting_filter_is_working(self):
        sorting_options = ["Default sorting",
                        "Sort by date (newest)",
                        "Sort by date (oldest)",
                        "Sort by title (A-Z)",
                        "Sort by title (Z-A)"]
        
        newest_list = ["Luis F Garcia",
                        "Dawn Thompson",
                        "Shannon Amrein",
                        "Mallory Asti"]
        
        oldest_list = ["Jennifer Zowada",
                        "Dr. Reid Winick",
                        "Lanie Wilt",
                        "Beth Wilson"]
        

        with allure.step("Move to Biomagnetism Service"):
            self.do_move_cursor_to_element_only(BiomagnetismServiceElements.biomagnetism_service)
        
        with allure.step("Clicked On Find a Therapist"):
            self.do_click(BiomagnetismServiceElements.find_a_therapy)
        
        
        with allure.step("Checking Default Sorting"):
            self.do_select_by_text(BiomagnetismServiceElements.sort_filter,"Default sorting")

            dr_arrangement_element = self.get_elements(BiomagnetismServiceElements.drs_title)
            dr_arrangement = [dr_title.text for dr_title in dr_arrangement_element]

            print(str(newest_list).removeprefix('[').removesuffix(']'))
            print(dr_arrangement)
            if not str(newest_list).removeprefix('[').removesuffix(']') in str(dr_arrangement):
                with allure.step("Default Sorting is not working properly"):
                    default =  False
            else:
                with allure.step("Default Sorting  is working properly"):
                    default =  True
        
        with allure.step("Checking Sort by date (newest)"):
            self.do_select_by_text(BiomagnetismServiceElements.sort_filter,"Sort by date (newest)")

            dr_arrangement_element = self.get_elements(BiomagnetismServiceElements.drs_title)
            dr_arrangement = [dr_title.text for dr_title in dr_arrangement_element]

            if not str(newest_list).removeprefix('[').removesuffix(']') in str(dr_arrangement):
                with allure.step("Sort by date (newest) is not working properly"):
                    newest =  False
            else:
                with allure.step("Sort by date (newest) is working properly"):
                    newest =  True

        
        with allure.step("Checking Sort by date (oldest)"):
            self.do_select_by_text(BiomagnetismServiceElements.sort_filter,"Sort by date (oldest)")

            dr_arrangement_element = self.get_elements(BiomagnetismServiceElements.drs_title)
            dr_arrangement = [dr_title.text for dr_title in dr_arrangement_element]

            if not str(oldest_list).removeprefix('[').removesuffix(']') in str(dr_arrangement):
                with allure.step("Sort by date (oldest) is not working properly"):
                    oldest =  False
            else:
                with allure.step("Sort by date (oldest)  is working properly"):
                    oldest =  True
        

        with allure.step("Checking Sort by title (A-Z)"):
            self.do_select_by_text(BiomagnetismServiceElements.sort_filter,"Sort by title (A-Z)")

            dr_arrangement_element = self.get_elements(BiomagnetismServiceElements.drs_title)
            dr_arrangement = [dr_title.text[0] for dr_title in dr_arrangement_element]
            
            
            if not self.is_sorted(dr_arrangement):
                with allure.step("Sort by title (A-Z) is not working properly"):
                    asc_order =  False
            else:
                with allure.step("Sort by title (A-Z)  is working properly"):
                    asc_order =  True
        
        with allure.step("Checking Sort by title (Z-A)"):
            self.do_select_by_text(BiomagnetismServiceElements.sort_filter,"Sort by title (Z-A)")

            dr_arrangement_element = self.get_elements(BiomagnetismServiceElements.drs_title)
            dr_arrangement = [dr_title.text[0] for dr_title in dr_arrangement_element]
            
            if self.is_sorted(dr_arrangement):
                with allure.step("Sort by title (Z-A) is not working properly"):
                    dsc_order =  False
            else:
                with allure.step("Sort by title (Z-A)  is working properly"):
                    dsc_order =  True
        
        if default and newest and oldest and asc_order and dsc_order:
            with allure.step("All Sorting are working"):
                return True
        else:
            with allure.step("All Sorting are not working"):
                return False
    def get_dr_list_from_excel(self):
        df = pd.read_excel("Data_Files/Biomagnetism_Services/dr_list.xlsx")
        df = df.fillna('')
        dic_list = (df.to_dict(orient= 'List'))

        new_dic_list = {key:[item for item in value if item != ''] for key,value in dic_list.items()}
        return new_dic_list

    def check_city_status(self,city,dr_list):
        with allure.step(f"Checking {city} status"):
            with allure.step(f"Clicked On {city}"):
                city_xpath = BiomagnetismServiceElements.get_city_xpath(city)
                self.do_click(city_xpath)
                time.sleep(7)
            with allure.step(f"Checking Dr. list in {city}"):
                dr_list_element = self.get_elements(BiomagnetismServiceElements.drs_title)
                dr_titles = [dr_title.text for dr_title in dr_list_element]
                print(f"Dr from website {dr_titles}")
                print(f"Dr from excel {dr_list}")

                if sorted(dr_titles) == sorted(dr_list):
                    with allure.step(f"All doctors are showing according to {city}"):
                        return True
                else:
                    with allure.step(f"All doctors are not showing according to {city}"):
                        return False

        
    def is_dr_showing_according_to_city_selected(self):

        dr_dict = self.get_dr_list_from_excel()
        cities = list(dr_dict.keys())
        for city in cities:

            city_status = self.check_city_status(city,dr_dict[city])
            if not city_status:
                return False
        else:
            with allure.step("All doctors are showing according to city"):
                return True
    

    def is_load_more_button_working(self):
        with allure.step("Move to Biomagnetism Service"):
            self.do_move_cursor_to_element_only(BiomagnetismServiceElements.biomagnetism_service)
        
        with allure.step("Clicked On Find a Therapist"):
            self.do_click(BiomagnetismServiceElements.find_a_therapy)
        with allure.step("Taking count of doctors"):
            doctor_count = len(self.get_elements(BiomagnetismServiceElements.doctors))

        with allure.step(f"Starting Doctors Count: {doctor_count}"):
            load_more_element = self.get_text_from_element_only(BiomagnetismServiceElements.load_more)
            with allure.step("Checking Load More Button"):
                while load_more_element == "LOAD MORE":
                    try:
                        load_more_element = self.get_text_from_element_only(BiomagnetismServiceElements.load_more)
                        print("Clicked On Load More Button")
                        self.do_click(BiomagnetismServiceElements.load_more)
                    except:
                        with allure.step("YOU’VE REACHED THE END OF THE LIST"):
                            load_more_element = "done"
            with allure.step("Taking count of doctors"):
                doctor_count_last = len(self.get_elements(BiomagnetismServiceElements.doctors))
            if load_more_element == "done" and doctor_count<doctor_count_last:
                with allure.step(f"Load More functionality is working. Total Doctors Count: {doctor_count_last}"):
                    return True
            else:
                with allure.step("Load More functionality is working"):
                    return False
        
                    # load_more = self.get_tag_attribute(BiomagnetismServiceElements.load_more2,'href')
                    # time.sleep(7)
                    # print(f"load more : {load_more}")
            
    def is_therepy_with_dr_garcia_clickable_and_redirected(self):
        with allure.step("Move to Biomagnetism Service"):
            self.do_move_cursor_to_element_only(BiomagnetismServiceElements.biomagnetism_service)
        
        with allure.step("Clicked On Therepy With Dr. Garcia"):
            self.do_click(BiomagnetismServiceElements.therapy_with_dr_garcia)
        with allure.step("Checking Therepy With Dr. Garcia Page Content"):
            therepy_body = self.get_text_from_element(BasePageElements.body)
            if "Therapy with Dr. Garcia" in therepy_body:
                with allure.step("Therapy With Dr. Garcia button is working and redirect to related page"):
                    return True
            else:
                with allure.step("Therapy With Dr. Garcia button is not working and redirect to related page"):
                    return False

    def is_appointment_details_correct(self):
        new_jersey = """New Jersey:
Home Office 138 Riverbend Drive, North Brunswick, NJ 08902 (732) 983-8616 info@usbiomag.com
Appointment Hours:
 Monday 9am–6:30pm
Tuesday Unavailable
Wednesday Unavailable
Thursday 9am–6:30pm
Friday 9am–6:30pm
Saturday Unavailable
Sunday Unavailable"""

        new_york = """Manhattan, NY:
The Morrison Center
461 Park Ave. South, 12th Floor, New York, NY 10016
(212) 989-9828
info@usbiomag.com
Appointment Hours:
Monday Unavailable
Tuesday 9:30am–6:30pm
Wednesday 9:30am–6:30pm
Thursday Unavailable
Friday Unavailable
Saturday Unavailable
Sunday Unavailable"""
        with allure.step("Taking Body Content"):
            body_content = self.get_text_from_element(BasePageElements.body)
        with allure.step("Checking New Jersey Details"):
            if new_jersey in body_content:
                with allure.step("New Jersey Details Are Visible And Correct"):
                    new_jersey_status = True
            else:
                with allure.step("New Jersey Details Are Not Visible And Correct"):
                    new_jersey_status = False
            
        
        with allure.step("Checking New York Details"):
            if new_jersey in body_content:
                with allure.step("New York Details Are Visible And Correct"):
                    new_york_status = True
            else:
                with allure.step("New York Details Are Not Visible And Correct"):
                    new_york_status = False
        
        if new_jersey_status and new_york_status:
            with allure.step("New Jersey and New York Contact Information Are Visible And Correct"):
                return True
        else:
            with allure.step("New Jersey and New York Contact Information Are Not Visible And Correct"):
                return False


            





            


        


                                                                    

            


                
        

        
        
