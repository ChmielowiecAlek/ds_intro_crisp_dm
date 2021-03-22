import urllib.request
import os
import shutil


class DataSource:
    __files = ['README.md', 'masculinity-survey.csv', 'masculinity-survey.pdf', 'raw-responses.csv']
    __target_dir = os.path.join('venv', 'data', 'masculinity_survey')

    @staticmethod
    def download_data():
        url_base = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/masculinity-survey/'
        try:
            shutil.rmtree(DataSource.__target_dir)
        except FileNotFoundError:
            pass
        os.makedirs(DataSource.__target_dir)
        for file in DataSource.__files:
            print('Downloading ' + file + ' from GitHub')
            target_path = os.path.join(DataSource.__target_dir, file)
            urllib.request.urlretrieve(url_base + file, target_path)
        print('Download completed')

    @staticmethod
    def get_data_path():
        data_file = DataSource.__files[3]
        return os.path.join(DataSource.__target_dir, data_file)


class MetaData:
    # The original metadata are in pdf format. Moreover, column names are ambiguous.
    __metadata = {'id': ('Sample number', None),
                  'start_date': ('Survey start date', None),
                  'end_date': ('Survey end date', None),
                  'DataSource_perception': (
                      'In general, how masculine or “manly” do you feel?',
                      ['Very masculine',
                       'Somewhat masculine',
                       'Not very masculine',
                       'Not at all masculine']
                  ),  # q0001
                  'perception_by_others': (
                      'How important is it to you that others see you as masculine?',
                      ['Very important',
                       'Somewhat important',
                       'Not too important',
                       'Not at all important']
                  ),  # q0002
                  'idea_source_father': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Father or father figure(s)',
                      ['Father or father figure(s)'
                       'Not selected']
                  ),  # q0004_0001
                  'idea_source_mother': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Mother or mother figure(s)',
                      ['Mother or mother figure(s)',
                       'Not selected']
                  ),  # q0004_0002
                  'idea_source_family': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Other family members',
                      ['Other family members',
                       'Not selected']
                  ),  # q0004_0003
                  'idea_source_pop_culture': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Pop culture',
                      ['Pop culture',
                       'Not selected']
                  ),  # q0004_0004
                  'idea_source_friends': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Friends',
                      ['Friends',
                       'Not selected']
                  ),  # q0004_0005
                  'idea_source_other': (
                      'Where have you gotten your ideas about what it means to be a good man? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0004_0006
                  'social_pressure': (
                      'Do you think that society puts pressure on men in a way that is unhealthy '
                      'or bad for them?',
                      ['Yes',
                       'No']
                  ),  # q0005
                  'frequency_ask_friend_professional': (
                      'How often would you say you do '
                      'Ask a friend for professional advice',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0001
                  'frequency_ask_friend_personal': (
                      'How often would you say you do '
                      'Ask a friend for personal advice',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0002
                  'frequency_male_affection': (
                      'How often would you say you do '
                      'Express physical affection to male friends, like hugging, '
                      'rubbing shoulders',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0003
                  'frequency_cry': (
                      'How often would you say you do '
                      'Cry',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0004
                  'frequency_fight': (
                      'How often would you say you do '
                      'Get in a physical fight with another person',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0005
                  'frequency_sex_women': (
                      'How often would you say you do '
                      'Have sexual relations with women, including anything '
                      'from kissing to sex',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0006
                  'frequency_sex_men': (
                      'How often would you say you do '
                      'Have sexual relations with men, including anything '
                      'from kissing to sex',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0007
                  'frequency_watch_sport': (
                      'How often would you say you do '
                      'Watch sports of any kind',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0008
                  'frequency_work_out': (
                      'How often would you say you do '
                      'Work out',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0009
                  'frequency_therapist': (
                      'How often would you say you do '
                      'See a therapist',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0010
                  'frequency_alienation': (
                      'How often would you say you do '
                      'Feel lonely or isolated',
                      ['Often',
                       'Sometimes',
                       'Rarely',
                       'Never, but open to it',
                       'Never, and not open to it']
                  ),  # q0007_0011
                  'worry_height': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your height',
                      ['Your height',
                       'Not selected']
                  ),  # q0008_0001
                  'worry_weight': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your weight',
                      ['Your weight',
                       'Not selected']
                  ),  # q0008_0002
                  'worry_hairline': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your hair or hairline',
                      ['Your hair or hairline',
                       'Not selected']
                  ),  # q0008_0003
                  'worry_physique': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your physique',
                      ['Your physique',
                       'Not selected']
                  ),  # q0008_0004
                  'worry_genitalia': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Appearance of your genitalia',
                      ['Appearance of your genitalia',
                       'Not selected']
                  ),  # q0008_0005
                  'worry_clothing': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your clothing or style',
                      ['Your clothing or style',
                       'Not selected']
                  ),  # q0008_0006
                  'worry_sex_perf': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Sexual performance or amount of sex',
                      ['Sexual performance or amount of sex',
                       'Not selected']
                  ),  # q0008_0007
                  'worry_mental_health': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your mental health',
                      ['Your mental health',
                       'Not selected']
                  ),  # q0008_0008
                  'worry_physical_health': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your physical health',
                      ['Your physical health',
                       'Not selected']
                  ),  # q0008_0009
                  'worry_finances': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your finances, including your current or future income, assets, or debt',
                      ['Your finances, including your current or future income, assets, or debt',
                       'Not selected']
                  ),  # q0008_0010
                  'worry_providing': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'Your ability to provide for your family, current or anticipated',
                      ['Your ability to provide for your family, current or anticipated',
                       'Not selected']
                  ),  # q0008_0011
                  'worry_none': (
                      'Which of the following do you worry about on a daily or near daily basis? '
                      'None of the above',
                      ['None of the above',
                       'Not selected']
                  ),  # q0008_0012
                  'employment_status': (
                      'Which of the following categories best describes your employment status?',
                      ['Employed, working full-time',
                       'Employed, working part-time',
                       'Not employed, student',
                       'Not employed-retired',
                       'Not employed, looking for work',
                       'Not employed, NOT looking for work']
                  ),  # q0009
                  'advantage_more_money': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men make more money',
                      ['Men make more money', 'Not selected']
                  ),  # q0010_0001
                  'advantage_taken_seriously': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men are taken more seriously',
                      ['Men are taken more seriously',
                       'Not selected']
                  ),  # q0010_0002
                  'advantage_more_choice': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men have more choice',
                      ['Men have more choice',
                       'Not selected']
                  ),  # q0010_0003
                  'advantage_more_development': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men have more promotion/professional development opportunities',
                      ['Men have more promotion/professional development opportunities',
                       'Not selected']
                  ),  # q0010_0004
                  'advantage_often_praised': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men are explicitly praised more often',
                      ['Men are explicitly praised more often',
                       'Not selected']
                  ),  # q0010_0005
                  'advantage_more_support': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Men generally have more support from their managers',
                      ['Men generally have more support from their managers',
                       'Not selected']
                  ),  # q0010_0006
                  'advantage_other': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0010_0007
                  'advantage_none': (
                      'Would you say it’s an advantage '
                      'to be a man at your work right now? '
                      'None of the above',
                      ['None of the above',
                       'Not selected']
                  ),  # q0010_0008
                  'disadvantage_women_preferred': (
                      'Would you say it’s a disadvantage '
                      'to be a man at your work right now? '
                      'Managers want to hire and promote women',
                      ['Managers want to hire and promote women',
                       'Not selected']
                  ),  # q0011_0001
                  'disadvantage_accusations_harassment': (
                      'Would you say it’s a disadvantage '
                      'to be a man at your work right now? '
                      'Greater risk of being accused of sexual harassment',
                      ['Greater risk of being accused of sexual harassment',
                       'Not selected']
                  ),  # q0011_0002
                  'disadvantage_accusations_sexism_racism': (
                      'Would you say it’s a disadvantage '
                      'to be a man at your work right now? '
                      'Greater risk of being accused of being sexist or racist',
                      ['Greater risk of being accused of being sexist or racist',
                       'Not selected']
                  ),  # q0011_0003
                  'disadvantage_other': (
                      'Would you say it’s a disadvantage '
                      'to be a man at your work right now? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0011_0004
                  'disadvantage_none': (
                      'Would you say it’s a disadvantage '
                      'to be a man at your work right now? '
                      'None of the above',
                      ['None of the above',
                       'Not selected']
                  ),  # q0011_0005
                  'harassment_confronted': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Confronted the accused person',
                      ['Confronted the accused person',
                       'Not selected']
                  ),  # q0012_0001
                  'harassment_hr_dept': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Contacted the HR department',
                      ['Contacted the HR department',
                       'Not selected']
                  ),  # q0012_0002
                  'harassment_manager': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Contacted the manager of the accused person',
                      ['Contacted the manager of the accused person',
                       'Not selected']
                  ),  # q0012_0003
                  'harassment_offer_support': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Reached out to the victim to offer support',
                      ['Reached out to the victim to offer support',
                       'Not selected']
                  ),  # q0012_0004
                  'harassment_not_responded': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Did not respond at all',
                      ['Did not respond at all',
                       'Not selected']
                  ),  # q0012_0005
                  'harassment_never_witnessed': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Never witnessed sexual harassment',
                      ['Never witnessed sexual harassment',
                       'Not selected']),  # q0012_0006
                  'harassment_other': (
                      'Have you seen or heard of a sexual harassment incident at your work? '
                      'If so, how did you respond? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0012_0007
                  'cause_if_not_responded': (
                      'And which of the following is the main reason you did not respond?',
                      ['You didn’t think it was your place',
                       'You weren’t sure who to contact',
                       'You didn’t want to get involved',
                       'You weren’t sure it was sexual harassment',
                       'Other: please specify']
                  ),  # q0013
                  'me_too_aware': (
                      'How much have you heard about the #MeToo movement?',
                      ['A lot',
                       'Some',
                       'Only a little',
                       'Nothing at all']
                  ),  # q0014
                  'me_too_impact_work': (
                      'As a man, would you say you think about your behavior at work '
                      'differently in the wake of #MeToo?',
                      ['Yes',
                       'No']
                  ),  # q0015
                  'make_first_move': (
                      'Do you typically feel as though you’re expected to make the first move '
                      'in romantic relationships?',
                      ['Yes',
                       'No']
                  ),  # q0017
                  'one_who_pays': (
                      'How often do you try to be the one who pays when on a date?',
                      ['Always',
                       'Often',
                       'Sometimes',
                       'Rarely',
                       'Never']
                  ),  # q0018
                  'pays_right_thing': (
                      'Which of the following are reasons '
                      'why you try to pay when on a date? '
                      'It’s the right thing to do',
                      ['It’s the right thing to do',
                       'Not selected']
                  ),  # q0019_0001
                  'pays_has_more_money': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'You make more money than your date',
                      ['You make more money than your date',
                       'Not selected']
                  ),  # q0019_0002
                  'pays_feel_good': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'You feel good about being the one who pays',
                      ['You feel good about being the one who pays',
                       'Not selected']
                  ),  # q0019_0003
                  'pays_social_expectations': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'Societal expectations, even though you don’t always think you should have to pay',
                      ['Societal expectations, even though you don’t always think you should have to pay',
                       'Not selected']
                  ),  # q0019_0004
                  'pays_initiator': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'You asked the person out, so you feel obligated to pay',
                      ['You asked the person out, so you feel obligated to pay',
                       'Not selected']
                  ),  # q0019_0005
                  'pays_testing_other': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'You try to pay to see if the other person will offer to share in the cost',
                      ['You try to pay to see if the other person will offer to share in the cost',
                       'Not selected']
                  ),  # q0019_0006
                  'pays_other': (
                      'Which of the following are reasons why you try to pay when on a date? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0019_0007
                  'interest_body_language': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'Read their physical body language to see if they are interested',
                      ['Read their physical body language to see if they are interested',
                       'Not selected']
                  ),  # q0020_0001
                  'interest_verbal_consent': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'Ask for a verbal confirmation of consent',
                      ['Ask for a verbal confirmation of consent',
                       'Not selected']
                  ),  # q0020_0002
                  'interest_check_reaction': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'Make a physical move to see how they react',
                      ['Make a physical move to see how they react',
                       'Not selected']
                  ),  # q0020_0003
                  'interest_it_depends': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'Every situation is different',
                      ['Every situation is different',
                       'Not selected']
                  ),  # q0020_0004
                  'interest_not_clear': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'It isn’t always clear how to gauge someone’s interest',
                      ['It isn’t always clear how to gauge someone’s interest',
                       'Not selected']
                  ),  # q0020_0005
                  'interest_other': (
                      'When you want to be physically intimate with someone, how do you gauge '
                      'their interest? '
                      'Other (please specify)',
                      ['Other (please specify)',
                       'Not selected']
                  ),  # q0020_0006
                  'boundaries_wondered': (
                      'Over the past 12 months, when it comes to sexual boundaries, have you done '
                      'Wondered whether you pushed a partner too far in a past sexual encounter.',
                      ['Wondered whether you pushed a partner too far in a past sexual encounter.',
                       'Not selected']
                  ),  # q0021_0001
                  'boundaries_talked_with_friend': (
                      'Over the past 12 months, when it comes to sexual boundaries, have you done '
                      'Talked with a friend or friends about whether you pushed a partner too far.',
                      ['Talked with a friend or friends about whether you pushed a partner too far.',
                       'Not selected']),  # q0021_0002
                  'boundaries_contacted_past_partner': (
                      'Over the past 12 months, when it comes to sexual boundaries, have you done '
                      'Contacted a past sexual partner to ask whether you went too far in any '
                      'of you sexual encounters.',
                      ['Contacted a past sexual partner to ask whether you went too far in any '
                       'of you sexual encounters.',
                       'Not selected']
                  ),  # q0021_0003
                  'boundaries_none': (
                      'Over the past 12 months, when it comes to sexual boundaries, have you done '
                      'None of the above',
                      ['None of the above',
                       'Not selected']
                  ),  # q0021_0004
                  'me_too_impact_relationships': (
                      'Have you changed your behavior in romantic relationships in the wake '
                      'of #MeToo movement?',
                      ['Yes',
                       'No']
                  ),  # q0022
                  'marital_status': (
                      'Are you now married, widowed, divorced, separated, or have you never '
                      'been married?',
                      ['Married',
                       'Widowed',
                       'Divorced',
                       'Separated',
                       'Never married']
                  ),  # q0024
                  'children_minor': (
                      'Yes, one or more children under 18',
                      ['Yes, one or more children under 18',
                       'Not selected']
                  ),  # q0025_0001
                  'children_adult': (
                      'Yes, one or more children 18 or older',
                      ['Yes, one or more children 18 or older',
                       'Not selected']
                  ),  # q0025_0002
                  'children_none': (
                      'No children',
                      ['No children',
                       'Not selected']
                  ),  # q0025_0003
                  'sexual_orientation': (
                      'Would you describe your sexual orientation as',
                      ['Straight',
                       'Gay',
                       'Bisexual',
                       'Other']
                  ),  # q0026
                  'race': (
                      'Are you',
                      ['White',
                       'Black',
                       'Hispanic',
                       'Asian',
                       'Other']
                  ),  # q0028
                  'education': (
                      'What is the last grade of school you completed?',
                      ['Did not complete high school',
                       'High school or G.E.D.'
                       'Associate’s degree'
                       'Some college'
                       'College graduate'
                       'Post graduate degree']
                  ),  # q0029
                  'us_state': (
                      'What state do you live in?',
                      ['New York',
                       'Not selected']
                  ),  # q0030
                  # the following are not described in the pdf
                  # some of them look like repetitions
                  'q0034': (
                      '? Income',
                      ['$0-$9,999',
                       'Not selected']
                  ),  # q0034
                  'q0035': (
                      '? Time Zone',
                      ['Middle Atlantic',
                       'Not selected']
                  ),  # q0035
                  'q0036': (
                      '? Machine',
                      ['Windows Desktop / Laptop',
                       'Not selected']
                  ),  # q0036
                  'race2': (
                      '? Skin colour',
                      ['Non-white',
                       'Not selected']
                  ),  # race2,
                  'racethn4': (
                      '? Ethnicity',
                      ['Hispanic',
                       'Not selected']
                  ),  # racethn4
                  'educ3': (
                      '? Educ 3',
                      ['College or more',
                       'Not selected']
                  ),  # educ3
                  'educ4': (
                      '? Educ 4',
                      ['College or more',
                       'Not selected']
                  ),  # educ4
                  'age3': (
                      '? Age interval',
                      ['35 - 64',
                       'Not selected']
                  ),  # age3
                  'kids': (
                      '? Kids',
                      ['No children',
                       'Not selected']
                  ),  # kids
                  'orientation': (
                      '? Orientation',
                      ['Gay/Bisexual',
                       'Not selected']
                  ),  # orientation
                  'weight': (
                      '? Weight',
                      None
                  ),  # weight
                  }

    @staticmethod
    def get_column_names():
        return MetaData.__metadata.keys()

    @staticmethod
    def get_description(column_name):
        return MetaData.__metadata[column_name][0]

    @staticmethod
    def get_allowed_values(column_name):
        return MetaData.__metadata[column_name][1]
