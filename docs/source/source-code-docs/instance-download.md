# Scraper Code

The function below were used to scrape the content from [jjvh.nl](http://jobshop.jjvh.nl/) and convert them into a python files.
The purpose of this scraper is automate the process of fetching JSP instances from the website and convert them into a 
format that can be imported as a python package.

```{warning}
[jjvh.nl](http://jobshop.jjvh.nl/) is frequently down. If the website is down, the scraper will not work.
```

```{tip}
All python file in the package '_download_instances_to_project' have a main function that can be executed to showcase 
the functionality of the file and its functions.
```


```{eval-rst} 
.. autofunction:: _download_instances_to_project.downloader::download_instances

```

```{eval-rst} 
.. automodule:: _download_instances_to_project.instance_details_downloader
   :members:

```

```{eval-rst} 
.. automodule:: _download_instances_to_project.python_file_writer
   :members:

```