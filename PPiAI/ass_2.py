# Storing the user values
print("Enter your username:")
user_name = str(input())
print("What is your checking account balance:")
checking_account_balance = float(input())
print("What is your savings account balance:")
savings_account_balance = float(input())
print("What is your investment account value:")
investment_account_value = float(input())
print("What is your total utility bills:")
total_utility_bills = float(input())
print("What is your total credit card debt:")
total_credit_card_debt = float(input())
print("What is your credit card balance due:")
credit_card_balance_due = float(input())
print("What is your credit card minimum payment due:")
credit_card_minimum_payment_due = float(input())
print("What is your credit card interest rate:")
annual_credit_card_interest_rate = float(input())
print("What is your loan debt:")
loan_debt = float(input())
print("What is your loan payment due:")
loan_payment_due = float(input())
print("What is your annual loan interest rate:")
annual_loan_interest_rate = float(input())
print("What is the value of other assets:")
other_asset_value = float(input())

# Formulas
total_value_of_assets = checking_account_balance + savings_account_balance + investment_account_value + \
                        other_asset_value
total_debt = total_utility_bills + total_credit_card_debt + loan_debt
total_net_worth = total_value_of_assets - total_debt
total_value_of_bills_due = total_utility_bills + credit_card_balance_due + loan_payment_due
value_remaining_in_the_checking_account_after_making_payments = checking_account_balance - total_value_of_bills_due
total_remaining_money_in_bank = value_remaining_in_the_checking_account_after_making_payments + savings_account_balance
credit_card_debt_after_paying_balance_due = total_credit_card_debt - credit_card_balance_due
loan_debt_after_paying_amount_due_add_interest = loan_debt - loan_payment_due + ((loan_debt - loan_payment_due) *
                                                                                 annual_loan_interest_rate / 12)
total_debt_after_making_payments = loan_debt_after_paying_amount_due_add_interest + \
                                   credit_card_debt_after_paying_balance_due
net_worth_after_making_payments_specified = total_value_of_assets - total_value_of_bills_due - \
                                            credit_card_debt_after_paying_balance_due - \
                                            loan_debt_after_paying_amount_due_add_interest
minimum_bills_due = total_utility_bills + credit_card_minimum_payment_due + loan_payment_due
value_remaining_in_checking_account_after_making_minimum_payments = checking_account_balance - minimum_bills_due
total_remaining_money_in_bank_2 = checking_account_balance + savings_account_balance - minimum_bills_due
interest_accrued_on_credit_balance_for_the_month = (credit_card_balance_due - credit_card_minimum_payment_due) * \
                                                   (annual_credit_card_interest_rate / 12)
total_credit_debt_after_paying_and_accruing_interest = total_credit_card_debt - credit_card_minimum_payment_due + \
                                                       interest_accrued_on_credit_balance_for_the_month
total_debt_after_making_payments_2 = total_credit_debt_after_paying_and_accruing_interest + \
                                     loan_debt_after_paying_amount_due_add_interest
net_worth_after_making_payments_specified_2 = total_value_of_assets - total_utility_bills - loan_payment_due - \
                                              credit_card_minimum_payment_due - \
                                              loan_debt_after_paying_amount_due_add_interest - \
                                              total_credit_debt_after_paying_and_accruing_interest

#Output Generated

print (f'Hello {user_name},')
print(" ")
print(f"The total dollar value of assets you own is ${total_value_of_assets} and the total dollar value of your debt is "
      f"currently ${total_debt}; therefore, your current net worth is: ${total_net_worth}.")
print(" ")
print(f"Your total bills due are ${total_value_of_bills_due}. Once you make these payments, you will have "
      f"${value_remaining_in_the_checking_account_after_making_payments} left in your checking account, and "
      f"${total_remaining_money_in_bank} in your bank overall. Additionally, your total credit card debt will be down "
      f"to ${credit_card_debt_after_paying_balance_due} and your loan debt will be "
      f"${loan_debt_after_paying_amount_due_add_interest}, including interest applied on the remaining balance after "
      f"your payment. Therefore, your total debt will then be paid down to ${total_debt_after_making_payments} "
      f"and your net worth will be ${net_worth_after_making_payments_specified}.")
print(" ")
#Optional Section
print(f"If you instead choose not to pay off your full credit card balance due, ${credit_card_balance_due}, and only "
      f"pay the minimum payment due, ${credit_card_minimum_payment_due}, you will have "
      f"${value_remaining_in_checking_account_after_making_minimum_payments} left in your checking account, and "
      f"${total_remaining_money_in_bank_2} in your bank overall. However, you will accrue "
      f"${interest_accrued_on_credit_balance_for_the_month}. Your total credit card debt will then be "
      f"${total_credit_debt_after_paying_and_accruing_interest}. In this case, your total debt would instead be "
      f"${total_debt_after_making_payments_2} and your net worth will be ${net_worth_after_making_payments_specified_2}.")
