# Devops Home Assignment - Shira Dahan

This repository contains a sample calculator application implemented in Python, along with a Jenkins pipeline to build, test, and deploy the application. The project demonstrates the integration of Jenkins pipelines, Git version control, and basic unit testing.

## Project Structure

The repository is organized as follows:

```
/                                # Repository root
|-- files/                       # Directory for application files
|   |-- SampleApplication.py     # Main calculator application
|   |-- testSampleApplication.py # test applications
|   |-- requirements.txt         # List of required Python packages
|   |-- jenkins_log_example.txt  # The final output of Jenkins pipeline

|
|-- Jenkinsfile             # Declarative Jenkins pipeline configuration
|-- README.md               # Project documentation
```

## Sample Application

The `SampleApplication.py` file contains a basic calculator application with two functions: `add_numbers` and `multiply_numbers`.
The `testSampleApplication.py` includes unittests to verify the accuracy of these functions.
I added the final output of the Jenkins pipline.

## Jenkins Pipeline

The `Jenkinsfile` defines a three-stage pipeline:

1. **Build**: Installs required Python packages from `requirements.txt`.
2. **Test**: Executes the unittests defined in `testSampleApplication.py`.
3. **Deploy**: Executes `SampleApplication.py` with various arguments.

## Running the Pipeline

To run the Jenkins pipeline:

1. Create a new Jenkins pipeline job.
2. Connect the job to your Git repository.
3. Specify the `Jenkinsfile` in the repository as the pipeline configuration.
4. Trigger the pipeline job execution.

## Notes

- Unittests are executed as part of the pipeline's test stage. Test results are displayed in the Jenkins console output.
- The pipeline can be customized to accommodate your specific needs.
- Ensure that your Git repository is properly integrated with Jenkins.

---
