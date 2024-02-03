import inquirer

def questions():
  responses = []
  location = [
    inquirer.List('location',
                  message = "Set your location",
                  choices = ['Fort McMurray', 'Vancouver', 'Beijing'],
              ),
  ]
  answers = inquirer.prompt(location)
  responses.append(answers['location'])

  fire_range = [
    inquirer.List('Fire Range',
                  message = 'Range of Fire',
                  choices = ['1','2','3','4','5'],
              ),
  ]
  answers = inquirer.prompt(fire_range)

  if answers['Fire Range'] == '1':
    fire_range = 10
  elif answers['Fire Range'] == '2':
      fire_range = 100
  elif answers['Fire Range'] == '3':
      fire_range = 500
  elif answers['Fire Range'] == '4':
      fire_range = 1000
  else:
      fire_range = 2000
  responses.append(fire_range)

  difficulty = [
    inquirer.List('Difficulty',
                  message = 'Difficulty to Contain',
                  choices = ['1','2','3','4','5'],
              ),
  ]
  answers = inquirer.prompt(difficulty)
  responses.append(int(answers["Difficulty"]))

  severity = [
    inquirer.List('Severity',
                  message = 'Severity of Fire',
                  choices = ['1','2','3','4','5'],
              ),
  ]
  answers = inquirer.prompt(severity)
  responses.append(int(answers["Severity"]))
                  
  return responses