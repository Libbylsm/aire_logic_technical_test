def medi_score_calculation(air_or_oxygen, consciousness, respiration_rate, spo2, temperature, cbg, fasting, previous_scores):
# cbg and fasting parameters are for the CBG bonus task
# previous_scores is for the alerting for trends in medi score bonus task (list of previous medi scores within last 24 hours)

    medi_score = 0

    # Air or Oxygen?
    medi_score += air_or_oxygen
    # 2 if oxygen is given, 0 if air is given

    # Consciousness
    if consciousness != 0:
        medi_score += 3 
        # 0 if alert, add 3 if CVPU

    # Respiration Rate
    if respiration_rate <= 8:
        medi_score += 3
    elif respiration_rate in range(9,12):
        medi_score += 1
    elif respiration_rate in range(21,25):
        medi_score += 2
    elif respiration_rate >= 25:
        medi_score += 3

    # SpO2
    # Patient is on air
    if air_or_oxygen == 0:
        if spo2 <= 83:
            medi_score += 3
        elif spo2 in range(84,86):
            medi_score += 2
        elif spo2 in range(86,88):
            medi_score += 1
        elif spo2 >= 93:
            medi_score += 0 # range is normal

    # Patient is on oxygen
    else:
        if spo2 <= 83:
            medi_score += 3
        elif spo2 in range(84,86):
            medi_score += 2
        elif spo2 in range(86,88):
            medi_score += 1
        elif spo2 in range(88,93):
            medi_score += 0 # range is normal
        elif spo2 in range(93,95):
            medi_score += 1
        elif spo2 in range(95,97):
            medi_score += 2
        elif spo2 >= 97:
            medi_score += 3

    # Temperature
    if temperature <= 35.0:
        medi_score += 3
    elif 35.1 <= temperature <= 36.0:
        medi_score += 1
    elif 36.1 <= temperature <= 38.0:
        medi_score += 0 # range is normal
    elif 38.1 <= temperature <= 39.0:
        medi_score += 1
    elif temperature >= 39.1:
        medi_score += 2

    # CBG (capillary blood glucose) bonus task
    if fasting: # if fasting
        if cbg <= 3.4:
            medi_score += 3
        elif 3.5 <= cbg <= 3.9:
            medi_score += 2
        elif 4.0 <= cbg <= 5.4:
            medi_score += 0
        elif 5.5 <= cbg <= 5.9:
            medi_score += 1
        elif cbg >= 6.0:
            medi_score += 3
    else: # 2 hours after eating
        if cbg <= 4.5:
            medi_score += 3
        elif 4.6 <= cbg <= 5.8: # table says 4.5 - 4.8 for score 2. This is assuming it means 4.6 - 5.8
            medi_score += 2
        elif 5.9 <= cbg <= 7.8:
            medi_score += 0
        elif 7.9 <= cbg <= 8.9:
            medi_score += 2
        elif cbg >= 9.0:
            medi_score += 3

    
    # Alerting for trends in medi score bonus task
    increased_score = any(prev_score <= medi_score -2 for prev_score in previous_scores)
    
    return medi_score, increased_score


# Examples (added last three arguments for the bonus task)
patient1 = medi_score_calculation(0, 0, 15, 95, 37.1, 5.0, True, [0,1])
patient2 = medi_score_calculation(2, 0, 17, 96, 37.1, 5.5, False, [2,3])
patient3 = medi_score_calculation(2, 1, 23, 88, 38.5, 4.5, True, [4,6])


# Test cases
# Outputs after both bonus tasks (without cbg and fasting)
print("Patient 1's medi score is:", patient1) # 0, False
print("Patient 2's medi score is:", patient2) # 6, True
print("Patient 3's medi score is:", patient3) # 8, True



    