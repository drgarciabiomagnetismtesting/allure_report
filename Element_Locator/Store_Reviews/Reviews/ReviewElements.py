from selenium.webdriver.common.by import By

class ReviewElements:
    review_button = (By.XPATH,"(//span[@class='menu-text'][normalize-space()='Reviews'])[1]")
    all_disease = (By.XPATH,"(//ul[@class='uael-video__gallery-filters'])[1]/li")
    all_review_videos = (By.XPATH,"""(//div[@data-all-filters='["filter-lyme-disease","filter-thyroid-cancer","filter-back-pain","filter-pandas-syndrome","filter-autism-spectrum-disorder","filter-depression","filter-extreme-allergies","filter-severe-insomnia","filter-flu","filter-sport-injuries","filter-traumatic-brain-injuries","filter-bronquitis","filter-shattered-spine","filter-foot-pain","filter-yeast-infection","filter-spine-injury","filter-rhabdomyolysis","filter-terrible-back-pain","filter-ehlers-danlos-symdrome","filter-menieres-disease","filter-t--cell-lymphoma","filter-shoulder-pain","filter-brachial-plexus-injury","filter-significant-changes","filter-chronic-illness","filter-leg-pain","filter-difficulty-in-walking"]'])[1]/div/div[1]""")

    yt_play_pause_btn = (By.CLASS_NAME, 'ytp-play-button')
    video_current_progress = (By.CLASS_NAME, 'ytp-time-current')

    def get_each_disease_xpath(disease):
        disease_button = (By.XPATH,f"(//li[contains(@class,'uael-video__gallery-filter')][normalize-space()='{disease}'])[1]")
        disease_list = (By.XPATH,f"//h4[normalize-space()='{disease}']")
        return disease_button, disease_list

    def get_iframe_xpath(video_index):
        return (By.XPATH,f"""((//div[@data-all-filters='["filter-lyme-disease","filter-thyroid-cancer","filter-back-pain","filter-pandas-syndrome","filter-autism-spectrum-disorder","filter-depression","filter-extreme-allergies","filter-severe-insomnia","filter-flu","filter-sport-injuries","filter-traumatic-brain-injuries","filter-bronquitis","filter-shattered-spine","filter-foot-pain","filter-yeast-infection","filter-spine-injury","filter-rhabdomyolysis","filter-terrible-back-pain","filter-ehlers-danlos-symdrome","filter-menieres-disease","filter-t--cell-lymphoma","filter-shoulder-pain","filter-brachial-plexus-injury","filter-significant-changes","filter-chronic-illness","filter-leg-pain","filter-difficulty-in-walking"]'])[1]/div/div[1])[{video_index}]//iframe""")
