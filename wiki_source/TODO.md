Make sure that the site is getting generated. Generated output files should not be push to git remote. The HTML file from the content of this directory will be generated in CI pipeline. Post that it has to be push to a static website. Pin the name of the static website in readme section of the repository.

Q. Where this mkdocs outputs are getting stored? --> site folder in root directory will have all the generated HTML files. This has to be uploaded in a blob storage --> azure static web app.
