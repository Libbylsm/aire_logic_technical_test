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
    if spo2 <= 83:
        medi_score += 3
    elif spo2 in range(84,86):
        medi_score += 2
    elif spo2 in range(86,88):
        medi_score += 1
    elif spo2 in range(88,93):
        medi_score += 0

    