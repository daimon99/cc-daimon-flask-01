# {{cookiecutter.package_name}}

## install and run

  1. `pip isntall -r requirements.txt`
  2. `vi .env`
  
      ```
      FLASK_APP={{cookiecutter.package_name}}
      FLASK_ENV=production
      # FLASK_ENV=development
      ```
    
  3. `flask run`