def medi_score_calculation(air_or_oxygen, consciousness, respiration_rate, spo2, temperature):

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

    return medi_score


# Examples
patient1 = medi_score_calculation(0, 0, 15, 95, 37.1)
patient2 = medi_score_calculation(2, 0, 17, 96, 37.1)
patient3 = medi_score_calculation(2, 1, 23, 88, 38.5)


# Test cases
print("Patient 1's medi score is:", patient1) # 0
print("Patient 2's medi score is:", patient2) # 4
print("Patient 3's medi score is:", patient3) # 8



    