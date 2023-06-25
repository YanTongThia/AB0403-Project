
menu ="""
Welcome to AB0403 Team 8 Insurance Advisor Program.
We are honored to be providing this service to our clients.

Login with username and password, assigned previously.
If you are a new user, please select accordingly.
Password Hint: Course Code\n"""

health_menu = "\n"+"-"*60+"""
Welcome to the Health Module.
Within the theme of Health, we offer 3 types of insurance.
They are: Medical, Accident and Vaccination.
Please select which type of Insurance you are interest in. 
"""

wealth_menu = "\n"+"-"*60+"""
Welcome to the Wealth Module.
Within the theme of Wealth, we offer 3 types of insurance.
They are: Savings, Retirement and Investment.
Please select which type of Insurance you are interest in. 
"""

def get_int(message,error_message): 
    int_var = input(message) # asking user for input, with message
    while True: 
        try: #try to convert input to int 
            int(int_var)
        except ValueError: #if fail to convert, print error message
            print(error_message)
            int_var = input(message) 
        else: # execute when there is no error
            break
    int_var = int(int_var) #force type conversion, assigned back into same var
    return int_var #return data to user

def get_float(message,error_message): 
    float_var = input(message) # asking user for input, with message
    while True: 
        try: #try to convert input to int 
            float(float_var)
        except ValueError: #if fail to convert, print error message
            print(error_message)
            float_var = input(message)
        else: # execute when there is no error
            break
    float_var = float(float_var) #force data type conversion, assigned back into same var
    return float_var #return data to user
    
def get_str(message,error_message): 
    str_var = input(message) #asking user for input, with message
    while not str_var.isalpha(): #while user input does not only contain alphabets
        print(error_message)
        str_var = input(message)
    return str_var #return data to user
    
def get_Y_or_N(message,error_message): 
    Y_or_N_var = input(message) #asking user for input, with message
    while Y_or_N_var not in ["Y","N","y","n"]: #while user input does not only contain these alphabets
        print(error_message)
        Y_or_N_var = input(message)
    return Y_or_N_var #return data to user 

def accrued_amount(period,rate,pmt):
    accrued_amount = 0
    for each in range(period):
        accrued_amount += pmt
        accrued_amount *= (1+rate)
    return accrued_amount

def if_lessthan_zero_equal_zero(amount,less):
    if (amount - less) < 0:
        amount = 0
        return amount
    amount -= less
    return amount 

def log_in(): 
    username = input("\nUserID:")
    while username not in database.keys(): #referencing all the keys a.k.a UserID in database 
        print("Invalid UserID. Please try again. Note Capitalisation Sensitive.")
        username = input("UserID:")
    else: 
        print("UserID accepted.")
    password = "AB0403"
    user_password = input("Password:")
    
    while user_password != password: # condition for password approval
        print("Invalid Password. Please try again. Note Capitalisation Senstive. Hint: Course Code")
        user_password = input("Password:")
    else:
        print(f"Password Accepted. Welcome {database[username][0]}.\n") #welcome statement

    return username

def create_new_user(): 
    each_split = [] #empty list
    for each in database.keys(): # output of each: User1, User2 ...
        each_split.append(each.split("r")[1])
        # each.split("r"): [Use,1]
        # each.split("r")[1]: [1] , append this into the empty list
    print(f"Welcome User{int(max(each_split))+1}.") # find max value of the list, increment by 1 is next UserID
    return f'User{int(max(each_split))+1}' #return UserID
        
def create_user_info():
    user_info = [] # empty list
    name = input("Enter your full name:") # names may have " " or "/" within
    while not name.replace(" ","").replace("/","").replace("-","").isalpha(): # replace all " ", "/", "-" to ""
        print("Input only alphabets.")
        name = input("Enter your full name:")
    user_info.append(name) 
    age = get_int("Enter your age:","Enter only numeric whole numbers.")
    user_info.append(age)
    gender = input("Enter your gender. M/F:") # input may be capitalized or not
    while gender not in ["M","F","m","f"]: #condition to allow for not captialized
        print("Enter only M or F.")
        gender = input("Enter your gender. M/F:")
    user_info.append(gender.capitalize()) #capitalized before appending
    print(f"Weclome {name}. {username} has been created.\n")
    return user_info

def sum_list(list_to_sum): # list_to_sum = ["Medical","100","Vaccination","0","",""]
    sum_list_premium = [] 
    for each in range(0,len(list_to_sum),2): # each: "Medical","Vaccination",""...
        if list_to_sum[each] != "":
            sum_list_premium.append(float(list_to_sum[each+1])) # each+1: "100","0",""...
    return sum(sum_list_premium)
     
def policy_report(username):
    policy_list = database[username][3:] 
    report ="\n"+"-"*60+"""\nCustomer Insurance Policy Report
Note that report will return blank,
if you did not subscribe / plan to subscribe to any.\n
"""
    for each in range(0,len(policy_list),2): # same logic as sum_list()
        if policy_list[each] != "":
            report +=f"""Insurance Policy: {policy_list[each]:>15}
Annual Premium: {float(policy_list[each+1]):>17,.2f}\n
"""
    report +="-"*60+"\n"
    report += f"Sum of Policy Premium: {float(sum_list(policy_list)):>10,.2f}\n"
    report +="-"*60+"\n"
    return report
    
def remove_all():
    print("""To enable users to better plan their insurance coverage, 
users are allow to remove all policies within this program.
""")
    decision = get_Y_or_N("Do you want to clear all policies from policy list? Y/N:","Input only Y or N.")
    if decision in ["Y","y"]:
        edit_list = database[username][3:]
    
        while '' in edit_list:
            edit_list.remove('')
    
        for each in edit_list:
            database[username][database[username].index(each)] = ''
        
        print("All policies removed.\n")
        print("Modified Policy Report:",policy_report(username))
        
def amount_for_premiums():
    sum_of_premium = sum_list(database[username][3:])
    amount_min = 0.03*float(income) #3%
    amount_max = 0.10*float(income) #10%
    amount_min_less = if_lessthan_zero_equal_zero(amount_min,sum_of_premium)
    amount_max_less = if_lessthan_zero_equal_zero(amount_max,sum_of_premium)
    print(f"""We recommend only setting aside 3 to 10% of your income for insurance.\n
Income: ${float(income):,.2f}
3% to 10% of Income: ${amount_min:,.2f} - ${amount_max:,.2f}
Recommended Amount, Less Existing Premiums: ${amount_min_less:,.2f} - ${amount_max_less:,.2f}\n""")
    amount = get_float("Amount to set aside:$","Enter only numeric number.")
    return amount

def index_override_else_append(policy_type):
    decision = get_Y_or_N("Would you like to purchase this plan?", "Input only Y or N.")
    if decision in ["Y","y"]:
        premium = get_float("What is the premium you would like to pay?","Input a numeric number.")
        if policy_type in database[username]: #existing investment policy
            print(f"You already have an existing {policy_type} Policy. You may only subscribe to one of each type of Policy.")
            decision_1 = get_Y_or_N("Would you like to update existing Policy?","Input only Y or N.")
            if decision_1 in ["Y","y"]: 
                index = database[username].index(policy_type)
                database[username][index+1] = premium
                print("Policy has been successfully added.")
        else: # no existing investment policy
            try:
                index = database[username].index("")
                database[username][index] = policy_type
                database[username][index+1] = premium
                print("Policy has been successfully added.")
            except:
                database[username].append(policy_type)
                database[username].append(premium)
                print("Policy has been successfully added.")
        
def main():
    print("\nYou have entered the main program.\nWe offer policies in these two broad themes: Health and Wealth.")
    while True:
        choice = health_or_wealth()
        if choice in ["E","e"]:
            print("You have exit the main program.")
            break 
        elif choice in ["Health","health"]:
            health()
        elif choice in ["Wealth","wealth"]:
            wealth()
            
def health_or_wealth():
    
    health_or_wealth = input("Which theme would you like to explore? E to Exit.:")
    while health_or_wealth not in ["Health","health","Wealth","wealth","E","e"]:
        print("Enter only Health, Wealth or E.")
        health_or_wealth = input("Which theme would you like to explore? E to Exit.:")
        
    return health_or_wealth

def health():
    while True:
        print(health_menu)
        health_sub_cat = input("Which category would you like to explore?\nMedical, Accident or Vaccination. Input E to Exit.:")
        while health_sub_cat not in ["Medical","medical","Accident","accident","Vaccination","vaccination","E","e"]:
            print("Enter only Medical, Accident, Vaccination or E.")
            health_sub_cat = input("Which category would you like to explore?\nMedical, Accident or Vaccination. Input E to Exit.:")
        if health_sub_cat in ["E","e"]:
            print("You have exit the health module.\n")
            break
        elif health_sub_cat in ["Medical","medical"]:
            medical()
        elif health_sub_cat in ["Accident","accident"]:
            accident()
        elif health_sub_cat in ["Vaccination","vaccination"]:
            vaccination()

def wealth():
    while True:
        print(wealth_menu)
        wealth_sub_cat = input("Which category would you like to explore?\nSavings, Retirement or Investment. Input E to Exit.:")
        while wealth_sub_cat not in ["Savings","savings","Retirement","retirement","Investment","investment","E","e"]:
            print("Enter only Savings, Retirement, Investment or E.")
            wealth_sub_cat = input("Which category would you like to explore?\nSavings, Retirement or Investment. Input E to Exit.:")
        if wealth_sub_cat in ["E","e"]:
            print("You have exit the wealth module.\n")
            break
        elif wealth_sub_cat in ["Savings","savings"]:
            savings()
        elif wealth_sub_cat in ["Retirement",'retirement']:
            retirement()
        elif wealth_sub_cat in ["Investment",'investment']:
            investment()
            
def medical():
    
    medical_menu = """
We offer 3 plans under the category of Medical. 
They are Standard Plan, Plus Plan and Premier Plan.
"""
    standard_plan ="""
Standard Plan
- Public Hospitals
- 4 Bedded Ward
- Choice of Doctor from Public Hospitals
- Surgical Benefits coverage of $590 - $21,840
- Surgical Implants coverage of $9,800
- Cancer Treatment coverage of $5,200 per month / $880 - $6,210 per treatment
- Renal Dialysis coverage of $3,740 per month
- Annual Claim Limit of $200,000
- Lifetime Guaranteed Renewability
- Deductibles of $1,500 - $3,000
- Co-insurance of 10%
"""
    plus_plan = """
Plus Plan:
- Public Hospitals
- Single-bedded Ward
- Choice of Doctor from Public Hospitals
- Pre-Hospitalisation Treatment for up to 180 days preceding confinement or day surgery (As Charged)
- Post-Hospitalisation Treatment within 365 days after Confinement or Day Surgery (As Charged)
- Annual Claim Limit of $600,000
- Lifetime Guaranteed Renewability
- Deductible of $1,500 - $5,250
- Co-insurance of 10% 
"""
    premier_plan = """
Premier Plan:
- Public + Private Hospitals
- Single-bedded Ward
- Choice of Doctor from any Hospital
- Pre-Hospitalisation Treatment for up to 180 days preceding confinement or day surgery (As Charged)
- Post-Hospitalisation Treatment within 365 days after Confinement or Day Surgery (As Charged)
- Annual Claim Limit of $1,200,000
- Lifetime Guaranteed Renewability
- Deductible of $1,500 - $5,250
- Co-insurance of 10%
"""
    print(medical_menu,standard_plan, plus_plan, premier_plan) 
    
    while True:
        medical_qn="""Option a: standard plan
Option b: plus plan
Option c: premier plan
Which medical plan would you want to explore? (a/b/c):"""
        plan_type = get_str(medical_qn,"Input only alphabets.")
        if plan_type not in ["a","b","c"]:
            print("Choose only Option a, b or c.")
            plan_type = get_str(medical_qn,"Input only alphabets.")
        age= int(database[username][1])
    
    # medical standard plan:
        if plan_type == "a":
            if 1<=age<=20:
                annual_premium= 40/12
            elif 21<=age<=40:
                annual_premium= 50/12
            elif 41<=age<=55:
                annual_premium= 120/12
            elif 56<=age<=65:
                annual_premium= 300/12
            elif 66<=age<=80:
                annual_premium = 500/12
            elif age>= 85:
                annual_premium= 1000/12
            print(f"\nThe monthly premium for standard plan at Age {age} is ${annual_premium:,.2f}.")
        
            decision = get_Y_or_N("\nWould you like to explore other plans?","Input only Y or N.")
            if decision in ["Y","y"]:
                break
    
    # medical Plus Plan:
        if plan_type == "b":
            if 1<=age<=20:
                annual_premium= 200/12
            elif 21<=age<=40:
                annual_premium= 300/12
            elif 41<=age<=55:
                annual_premium= 600/12
            elif 56<=age<=65:
                annual_premium= 1000/12
            elif 66<=age<=80:
                annual_premium = 2000/12
            elif age>= 85:
                annual_premium= 3500/12
            print(f"\nThe monthly premium for Plus Plan at Age {age} is ${annual_premium:,.2f}.")
            
            decision = get_Y_or_N("\nWould you like to explore other plans?","Input only Y or N.")
            if decision in ["Y","y"]:
                break
            
    # PruShield Premier Plan:       
        if plan_type == "c":
            if 1<=age<=20:
                annual_premium= 215/12
            elif 21<=age<=40:
                annual_premium= 320/12
            elif 41<=age<=55:
                annual_premium= 655/12
            elif 56<=age<=65:
                annual_premium= 1200/12
            elif 66<=age<=80:
                annual_premium = 2500/12
            elif age>= 85:
                annual_premium= 4000/12
            print(f"\nThe monthly premium premier plan at Age {age} is ${annual_premium:,.2f}.")
            
            decision = get_Y_or_N("\nWould you like to explore other plans?","Input only Y or N.")
            if decision in ["Y","y"]:
                break
    
    index_override_else_append("Medical")

def accident():
    print("""For accident plans, policy holders will get a reimbursement on Accidental Death and Dismemberment; Medical reimbursement per accident or disease and for accidents when using public or private transport.
Each plan would require different montly premiums, which would affect the amount of reimursement a policy holder is entitled to for each respective accidents.""")     
    while True:
        print(f"Your monthly income is {float(income):,.2f}.")
        preferred_payment = get_float(f"How much of your Monthly Amount ${amount:,.2f} do you wish to allocate to your accident plan?","Enter only numeric number.")
        
        if preferred_payment < 175:
            print("The minimum amount for monthly premium is $175.")
            decision = get_Y_or_N("Do you wish to view other plans? Y/N:","Input only Y or N.")
            if decision in ["Y",'y']:
                break
            
        if 175<=preferred_payment<=369:
            print("I would reccomend Plan A. By just paying $175 a year, you would get $100,000 payout on Accidental Death and Dismemberment; Medical reimbursement of up to $2000 per accident or disease; $300,000 payout for accidents when using public or private transport.")
            decision = get_Y_or_N("Do you wish to view other plans? Y/N:","Input only Y or N.")
            if decision in ["Y",'y']:
                index_override_else_append("Accident")
                break
            
        elif 370<= preferred_payment <= 569:
            print("I would reccomend Plan B. By just paying $370 a year, you would get $300,000 payout on Accidental Death and Dismemberment; Medical reimbursement of up to $4000 per accident or disease; $600,000 payout for accidents when using public or private transport.")
            decision = get_Y_or_N("Do you wish to view other plans? Y/N:","Input only Y or N.")
            if decision in ["Y",'y']:
                index_override_else_append("Accident")
                break
            
        elif 570<= preferred_payment :
            print("I would reccomend Plan C. By just paying $570 a year, you would get $500,000 payout on Accidental Death and Dismemberment; Medical reimbursement of up to $6000 per accident or disease; $800,000 payout for accidents when using public or private transport ")
            decision = get_Y_or_N("Do you wish to view other plans? Y/N:","Input only Y or N.")
            if decision in ["Y",'y']:
                index_override_else_append("Accident")
                break
    
def vaccination():
    print("This is a free complimentary financial protection upon hospitalisation due to the side effects of COVID-19 vaccinations.") 
    print(f"""The following information will be shared with relevant authorities as required for this policy.
Name: {database[username][0]}
Age: {database[username][1]}
Gender: {database[username][2]}""")
    if int(database[username][1]) < 18:
        print("You will need your gaurdian/parent to sign up for you.")
    vaccination = get_Y_or_N('Are you fully vaccinated? Y/N:',"Input only Y or N.")
    if vaccination in ["Y",'y']:
        print("This policy will cover you for any and all booster shots you may choose to take.")
    if vaccination in ["N",'n']:
        print("This policy will cover you for any and all vaccination shots you may choose to take.")
    decision = get_Y_or_N("Would you like to purchase this plan?", "Input only Y or N.")
    if database[username][3] != "": #existing insurance policy  
        if decision in ["Y","y"]: 
            if "Vaccination" in database[username]: #existing vaccination policy
                print("You already have an existing Vaccination Policy. You may only subscribe to one of each type of Policy.")             
            else: #no existing vaccination policy, but existing insurance policy
                database[username].append("Vaccination")
                database[username].append("0")
                print("Policy has been successfully added.")
    else: #no existing insurance policy
        print("You will have to apply for other policies to be entilted to this free coverage.")
        
def savings():
    #Choose whether to explore PRUActive Saver III plan
    print("We have 2 Savings plan: Saver and Cash\n")
    explore_saver = get_Y_or_N("Would you like to explore Saver Plan? Y/N:", "Input only Y or N.")
    
    if explore_saver in ["Y","y"]:
        while True:

            #intro plan
            print("""Saver Plan is a customisable insurance savings plan that will suit your unique needs, no matter if your goals are big or small, 
for now or for the future. You can decide how much savings you want to set aside, the savings’ duration and when your maturity payout would be.
Be worry free with a plan that offers capital guaranteed with lump sum payout at maturity. \n""")

            #collect appropriate data from user   
            #Customise your plan's policy term i.e. from 10yr to 30yr
            print("Depending on your goals, you can customise your plan’s policy term from 5 to 30 years. Receive your maturity payout when you need it.\n")
                      
            regular_premium_term = get_int("Please input Regular Premium term (5 to 30 years):","Enter only numeric whole numbers.")

            #error checking
            while regular_premium_term<5 or regular_premium_term>30:
                print("Regular premium term should be between 5 and 30 years!\n")
                regular_premium_term = get_int("Please input Regular Premium term (5 to 30 years):","Enter only numeric whole number.")

                    
            monthly_regular_premium_amount = get_float("Please input monthly Regular Premium amount:","Enter only numeric number.")

            #Maturity value
            accrued_amount = 0
            interest_rate = 0.03 #start at 3%, increases by 0.1% every year
            for each in range(regular_premium_term * 12):  
                accrued_amount += monthly_regular_premium_amount   #add monthly premium
                accrued_amount *= (1.0+(interest_rate/12)) #compounded monthly

                if (each%12==0 and each>0): #increase interest rate by 0.1% every year
                    interest_rate += 0.001
                        
                    
            regular_premium_at_maturity = accrued_amount #compounded monthly.
            print(f"At maturity, you will potentially receive {regular_premium_at_maturity:,.2f}\n")


                #Exit program?
            to_continue = get_Y_or_N("Would you like to continue exploring PRUActive Saver III? Y/N:", "Input only Y or N.")
            if to_continue in ["N","n"]:
                break



    #implementation for PRUActive cash below
    explore_cash = get_Y_or_N("Would you like to explore PRUActive Cash? Y/N:", "Input only Y or N.")

    if explore_cash in ["Y","y"]:
        while True:
                #intro
                print("""PRUActive cash an insurance savings plan with a yearly cash benefit.
PRUActive Cash gives you the flexibility and structure to meet today’s needs,
with tomorrow’s dreams in mind. \n""")

                #collect appropriate data from user
               
                    #Customise your plan's policy term i.e. from 5 yr to 25 yr
                print("Depending on your goals, you can customise your plan’s policy term from 5 to 25 years. Receive your maturity payout when you need it.\n")
                policy_term = get_int("Please enter the duration of your policy term:","Enter only numeric whole number.")

                    #error checking
                while policy_term<5 or policy_term>25:
                    print("Policy term should be between 5 and 25 years!\n")
                    policy_term = get_int("Please enter the duration of your policy term:","Enter only numeric whole number.")

                    
                    #monthly payment - choose amount to deposit monthly from 5 to 25 years
                print("You have the option to choose an amount to deposit per month.\n")
                Amount_chosen = get_float("How much would you wish to deposit monthly?:","Enter only numeric whole number.")

        
                    #option to withdraw cash
                print("You have the option to withdraw cash payment equivalent to 3% of your current savings or to let your current savings accumulate untouched for higher interest.\n")
                withdraw_cash_chosen = get_Y_or_N("Would you like to withdraw cash? Y/N: ","Input only Y or N.")
   
                    #withdraw_cash
                if (withdraw_cash_chosen in ["Y","y"]):
                    year = get_int("After how many years would you like to withdraw cash?:","Enter only numeric whole number.")

                    #error checking
                    while year > policy_term:
                        print("Your policy term has already ended by then!\n")
                        year = get_int("After how many years would you like to withdraw cash?:","Enter only numeric whole number.")
                    

                    #calculate total amount of cash withdrawn
                    accrued_amount = 0
                    for each in range(year*12):
                        accrued_amount += Amount_chosen
                        accrued_amount *= (1+(0.03/12))

                    cash_withdrawn = 0.03*accrued_amount
                    print(f"Cash withdrawn after {year} Years, will be {cash_withdrawn:,.2f}.\n")

                        #At maturity
                    accrued_amount -= cash_withdrawn
                    for each in range((policy_term-year)*12):
                        accrued_amount += Amount_chosen
                        accrued_amount *= (1+(0.03/12))
                        
                    print(f"At maturity, you will receive {accrued_amount:,.2f}\n")
                #Not withdrawing cash
                else: 
                    #At maturity
                    accrued_amount = 0
                    for each in range(policy_term*12):
                        accrued_amount += Amount_chosen
                        accrued_amount *= (1+(0.03/12))
                    
                    print(f"If no withdrawals are made, at maturity, you will receive ${accrued_amount:,.2f}.\n")
                    
                        
                to_continue = get_Y_or_N("Would you like to continue exploring PRUActive Cash?:", "Input only Y or N.")
                if to_continue in ["N","n"]:
                    break
                    
    index_override_else_append("Savings")
    
def retirement():       
    print("""We offer 2 retirement Plans.
          
(1) Retirement I (Covers retirement plan)

- Minimum $300 a month 
- Payout as early as 50 years old, monthly payment upon retirement (15 years)
- Attractive income bonuses (.1% bonus) and step up income (.5% bonus)
- 4% Investment rate of return
- Payout of $800 per month

(2) Retirement II (Covers retirement and accidental plan
- min $1500 a month
- 15 year premium payment 
- Payout of $1000 per month
- Additional CareFund that covers % of bills when sick
Daily Hospital Income Benefit
Daily ICU Benefit                  0.1% per day (Cap at S$750 per day)
Recovery Benefit                   0.1% per day (Cap at S$750 per day)
Outpatient Active Cancer Drug      1% (Cap at S$10,000 per injury/illness)
Treatment Benefit                  1% (Cap at S$5,000 per injury/illness)
Severe Surgical Benefit            2% (Cap at S$10,000 per injury/illness)
- Insured for 20 years upon choosen date 
- extra 0.3% bonus per month payout (of principal)
""")
    
    while True:
        choose = input("Which option would you like to explore more? (E to Exit) 1/2/E:")
        while choose not in ["1","2","E","e"]:
            print("Input only 1, 2 or E.")
            choose = input("Which option would you like to explore more? (E to Exit) 1/2/E:")
            
        if choose in ["E",'e']:
            break
        
        if choose == "1":
            print("Retirement I")
            premium = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
            while premium < 300:
                print("Premium has to be more than $300 per month")
                premium = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
            
            age = int(database[username][1])
            age_1 = get_int("Please enter age you would might retire:","Enter only numeric whole number.")
            
            while age_1 < age:
                print("Retire age must be older than current age.")
                age_1 = get_int("Please enter age you would might retire:","Enter only numeric whole number.")
                
            age_2 = age_1 - age
            x = 1000
            accrued = accrued_amount(age_2 * 12,0.0033,premium)
            print(f"Amount accumulated would be ${accrued:,.2f} after {age_2} years.")
            print(f"Amount you get per year including bonuses would be ${x + accrued * 0.006:,.2f}.")
            continue1 = get_Y_or_N("Would you like to explore option 2? Y/N:", "Input only Y or N.")
            if continue1 in ["y","Y"]:
                print("Retirement II")
                premium_1 = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
                while premium_1 < 1500:
                    print("Premium has to be more than $1500 per month")
                    premium_1 = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
                interest_1 = premium_1 * 12 * 15
                print(f"Amount invested would be ${interest_1:,.2f} after 15 years.")
                print(f"Amount you get per year would be ${1000 + interest_1 * 0.003:,.2f} after 20 years.")
            elif continue1 in ["n","N"]:
                break
                
            
        if choose == "2":
            print("Retirement II")
            premium_1 = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
            while premium_1 < 1500:
                print("Premium has to be more than $1500 per month")
                premium_1 = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
            interest_1 = premium_1 * 12 * 15
            print(f"Amount invested would be ${interest_1:,.2f} after 15 years.")
            print(f"Amount you get per year would be ${1000 + interest_1 * 0.003:,.2f} after 20 years.")
            continue1 = get_Y_or_N("Would you like to explore option 1? Y/N:","Input only Y or N.")
            if continue1 in ["y","Y"]:
                print("Retirement I")
                premium = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
                while premium < 300:
                    print("Premium has to be more than $300 per month")
                    premium = get_float("Please enter how much you would like to invest per month:$","Enter only numeric number.")
                
                age = int(database[username][1])
                age_1 = get_int("Please enter age you would might retire:","Enter only numeric whole number.")
                
                while age_1 < age:
                    print("Retire age must be older than current age.")
                    age_1 = get_int("Please enter age you would might retire:","Enter only numeric whole number.")
                    
                age_2 = age_1 - age
                x = 1000
                accrued = accrued_amount(age_2 * 12,0.0033,premium)
                print(f"Amount accumulated would be ${accrued:,.2f} after {age_2} years.")
                print(f"Amount you get per year including bonuses would be ${x + accrued * 0.006:,.2f}")
            elif continue1 in ["n","N"]:
                break
            
    index_override_else_append("Retirement")
    
    
def investment():
    print("""\nOur Investment plan offers wealth accumulation at 3% per annum.
          
Premium can be paid in 20 monthly installments. 

Minimum monthly premium of $300.

After 20 periods, you may make withdrawals of no more than $5,000 per year, 
where withdrawal amount is no more than 20% of total value in policy.

Any remaining amount left will protect against death at 110% of the remaining value. 
After death, the investment policy may be assigned to a dependent at your choosing.
""")

    while True:
        print("Lets explore how much value in policy after 20 periods of monthly contributions.\n")
        monthly_premium = get_float("Please input monthly premium amount:","Enter only numeric number.")
        accrued_amount = 0
        for each in range(20):
            accrued_amount += monthly_premium
            accrued_amount *= (1+0.03)
            print(f"At Period {each+1}, the amount in policy would be ${accrued_amount:,.2f}.")
        if int(database[username][1]) + 5 > 60:
            print(f"Assuming you do not withdraw any amount, when you are 60 Y0, the amount is policy would be ${accrued_amount(60-int(database[username][1]),0.03,monthly_premium):,.2f}\n")

        age_to_maturity = 60 - (int(database[username][1])+5)
        monthly_premium_at_60 = accrued_amount*(1+0.03)**(age_to_maturity)
        print(f"Assuming you do not withdraw any amount, when you are 60 Y0, the amount is policy would be ${monthly_premium_at_60:,.2f}\n")
        print(f"You will be insurred at 110% of ${monthly_premium_at_60:,.2f} at ${monthly_premium_at_60*1.1:,.2f}")
        index_override_else_append("Investment")
                
        to_continue = get_Y_or_N("Would you like to move on to explore other policies?:", "Input Y or N.")
        if to_continue in ["Y",'y']:
            break

def data_report():
    data_report_header = """
In line with our company's personal data policy, 
all user information will be presented in a personal data report.
The personal data report has been saved to your device.
    """
    print(data_report_header)
    
    data_report_content = f"""Dear {database[username][0]},
    
Thank you for using our product. We value your feedback. 
Please head over to Team8.AB0403.com to let us know how we can improve.\n"""
    
    data_report_content += data_report_header 
    data_report_content += policy_report(username)
    
    
    data_report_content +=f"""
Personal Data Report
Name: {database[username][0]}
Age: {database[username][1]}
Gender: {database[username][2]}
Income: {float(income):,.2f}
Monthly amount to be set aside for Insurance Premiums: {float(amount):,.2f}
"""
    
    sign_off = """\nYours Truly,
Team 8"""
    data_report_content += sign_off
    
    return data_report_content

####

import csv 

filename = "database.csv" 
database = {}

with open(filename, "r") as f: #reading database csv file 
    csv_pointer = csv.reader(f)
    for each in csv_pointer:
        database[each[0]] = each[1:] #creating dictionary; UserID as Key, Name Age Gender etc as Value in a list


print(menu) # Welcome menu

existing_account = get_Y_or_N("Do you have an existing account with us? Y/N:", "Input only Y or N.") # branching for login
if existing_account in ["y","Y"]:
    username = log_in() #log in for existing users
else:
    username = create_new_user() #creating new UserID
    UserInfo = create_user_info() #creating user information to populate database
    database[username] = UserInfo #assigning UserID to user information in database dictionary
            
print("To enable us to better tailor our recommendations, provide the neccessary information.\n")
income = get_float("Enter your monthly income?:$","Enter only numeric numbers.")

print("\nCurrent Policy Report:",policy_report(username))
remove_all()
amount = amount_for_premiums()

main()

print("\nUpdated Policy Report:",policy_report(username))
print("End of Program.")

data_report_name = "data_report.txt"
with open(data_report_name,"w") as f:
    f.write(data_report())

print("""If you are interested in any of policies above, please contact our insurance agents 
who will be able to help you purchase your required plans. Do remember to share your 
data report with our friendly agents to enable the discussion process.""")

# Updating Database with updated data (e.g. new users)
list1 = []
list2 = []
for key,value in database.items():   
    list1.append(key) #append key 
    for each in value: #for each value in value pair, append each
        list1.append(each)
    list2.append(list1) #append the list into the main list, list2
    list1 = [] #clear list1 for next key value pair
with open(filename, "w",newline='') as f: #writing list2 into csv database file, removing new lines 
      csv_pointer = csv.writer(f)
      csv_pointer.writerows(list2)
