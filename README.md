pip install allure-pytest     
python -m pytest --alluredir allure-results
allure serve allure-results

![img.png](img.png)

pip install behave
pip install pytest-bdd
pip install allure-behave

#make BDD directory,subdirectory features with subdirectory steps
#make .feature file and steps file

behave
behave -f allure_behave.formatter:AllureFormatter -o reports/ 
allure serve reports/
*******************************************************************************************
unittest: You define test cases directly in code, and assertions are used to verify outcomes. Reporting is enhanced with allure.
BDD: You define behavior in a natural language format (Gherkin), making it accessible to non-developers. Step definitions map the behavior to actual code.

![image](https://github.com/user-attachments/assets/e37836ed-426f-4e0e-b7bc-3c9d2cf76552)





![img_1.png](img_1.png)
#   u n i t t e s t _ t e s t i n g _ l o g i n p a g e 
 
 
