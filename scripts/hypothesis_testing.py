import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from scipy.stats import ttest_ind

class HypothesisTesting:
    def __init__(self, data):
        self.data = data

    
    def risk_difference_across_provinces(self):

        ## Calculate claims to Premium ratio 
        self.data['claims_to_premiums_ratio'] = self.data['TotalClaims'] / (self.data['TotalPremium'] + 1)

        ### Let's segment the data into provinces
        anova = [self.data[self.data['Province'] == province]['claims_to_premiums_ratio'] for province in self.data['Province'].unique()]

        ## Perform anova test

        ## Perform anova test

        anova_result = f_oneway(*anova)
        print("Test : ANOVA")
        print('T-test F-statistic:', anova_result.statistic)
        print('T-test p-value:', anova_result.pvalue)
        if anova_result.pvalue < 0.05:
            print("Reject the null hypothesis: There are significant risk differences across provinces.")
        else:
            print("Fail to reject the null hypothesis: No significant risk differences across provinces.")


    def risk_difference_across_zip_codes(self):

        ## Let's group the data randomly into 2 groups using the postal code
        unique_postal_codes = self.data['PostalCode'].unique()

        # Shuffle the postal codes
        np.random.shuffle(unique_postal_codes)

        # Split into two groups
        split_index = len(unique_postal_codes) // 2
        group1 = unique_postal_codes[:split_index]
        group2 = unique_postal_codes[split_index:]

        # Create a new column to indicate the group for each postal code
        self.data['group'] = self.data['PostalCode'].apply(lambda x: 'Group 1' if x in group1 else 'Group 2')

        # Extract claims-to-premiums ratio for each group
        group1_data = self.data[self.data['group'] == 'Group 1']['claims_to_premiums_ratio']
        group2_data = self.data[self.data['group'] == 'Group 2']['claims_to_premiums_ratio']

        # Perform independent t-test
        t_test_result = ttest_ind(group1_data, group2_data)
        print("Test: T-test")
        print('T-test T-statistic:', t_test_result.statistic)
        print('T-test p-value:', t_test_result.pvalue)

        if t_test_result.pvalue < 0.05:
            print("Reject the null hypothesis: There are significant risk differences between zip codes.")
        else:
            print("Fail to reject the null hypothesis: No significant risk differences between zip codes.")

    def profit_difference_across_zip_codes(self):

        ## Let's group the data randomly into 2 groups using the postal code
        unique_postal_codes = self.data['PostalCode'].unique()

        # Shuffle the postal codes
        np.random.shuffle(unique_postal_codes)

        # Split into two groups
        split_index = len(unique_postal_codes) // 2
        group1 = unique_postal_codes[:split_index]
        group2 = unique_postal_codes[split_index:]

        # Create a new column to indicate the group for each postal code
        self.data['group'] = self.data['PostalCode'].apply(lambda x: 'Group 1' if x in group1 else 'Group 2')

        ## Let's assume profit is calculated as the difference between Premium and claims
        self.data['Profit'] = self.data['TotalPremium'] - self.data['TotalClaims']

        # Extract claims-to-premiums ratio for each group
        group1_data = self.data[self.data['group'] == 'Group 1']['Profit']
        group2_data = self.data[self.data['group'] == 'Group 2']['Profit']

        # Perform independent t-test
        t_test_result = ttest_ind(group1_data, group2_data)
        print("Test: T-test")
        print('T-test T-statistic:', t_test_result.statistic)
        print('T-test p-value:', t_test_result.pvalue)

        if t_test_result.pvalue < 0.05:
            print("Reject the null hypothesis: There are significant Margin(Profit) differences between zip codes.")
        else:
            print("Fail to reject the null hypothesis: No significant Margin(Profit) differences between zip codes.")

    def risk_difference_across_gender(self):

        # Separate data by gender
        risk_men = self.data[self.data['Gender'] == 'Male']['claims_to_premiums_ratio']
        risk_women = self.data[self.data['Gender'] == 'Female']['claims_to_premiums_ratio']

        # Perform independent t-test
        t_test_result = ttest_ind(risk_men, risk_women)
        print('Test: T-test')
        print('T-test T-statistic:', t_test_result.statistic)
        print('T-test p-value:', t_test_result.pvalue)

        if t_test_result.pvalue < 0.05:
            print("Reject the null hypothesis: There are significant risk differences between women and men.")
        else:
            print("Fail to reject the null hypothesis: No significant risk differences between women and men.")

    