def risk_factor(distance,responses):
  gap = distance - responses[1]  # distance - range
  sev_ranges = [50,100,250,500,1000]

  if gap <= 0: # Inside the fire range
      if responses[2] > 2: # DtC is more than 2, very high risk regardless of Sev.
          return 'Very High Risk'

      elif responses[2] <= 2: # DtC is less than 2, very high risk if Sev > 2 else high risk.
          if responses[3] > 2:
              return 'Very High Risk'
          elif responses[3] <= 2:
              return 'High Risk'

  elif distance - (responses[1] + sev_ranges[responses[3]-1]) <= 0: # Outside the fire range but inside severity range.
      if responses[2] > 2: # DtC is more than 2,  regardless of Sev.
          return 'High Risk'

      elif responses[2] <= 2: # DtC is less than 2, very high risk if Sev > 2 else high risk.
          if responses[3] > 2:
              return 'High Risk'
          elif responses[3] <= 2:
              return 'Moderate Risk'

  else: # Outside fire and severity range.
      gap = distance - (responses[1] + sev_ranges[responses[3]-1])
      if gap < 1000:
          if responses[2] > 2: # DtC is more than 2,  regardless of Sev.
              return 'Moderate Risk'

          elif responses[2] <= 2: # DtC is less than 2, very high risk if Sev > 2 else high risk.
              if responses[3] > 2:
                  return 'Moderate Risk'
              elif responses[3] <= 2:
                  return 'Low Risk'
      else:
          return 'Low Risk'

      