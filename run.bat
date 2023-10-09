D:\seleniumFramework\ecomApp\Scripts\activate
cd D:\seleniumFramework
pytest -s -v -m "sanity" --html=./Reports/sanityReport.html testCases/ --browser chrome