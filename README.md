# SCA-API - Test task

## Requirements
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## How to Use

1. Clone the repository:
```bash
git clone https://github.com/ImperatorNeron/sca-api.git
cd your_repository
```
2. Install all required packages in **Requirements** section.
3. Set up environment variables. Create a .env file in the root directory and specify the required configurations. You can use .env.template.
4. Set up a virtual environment in the app directory and install 
```bash 
   pip install scons
   pip install poetry
   poetry install
   ```
5. Start the application using ```scons up``` and after that, run the database migrations ```scons migrate-up```.
6. Your project is now ready for use!

### Implemented Commands

#### Application
- ```scons up``` - up application
- ```scons logs``` - follow the logs in app container
- ```scons down``` - down application and all 

#### Database migrations
- ```scons auto-migrations``` - autocreate file of tables
- ```scons migrate-up``` - apply migrations to head
- ```scons migrate-down``` - down migrations t base

## License

This project is licensed under the MIT License - see the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.