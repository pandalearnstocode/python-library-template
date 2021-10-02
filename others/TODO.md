# List of things to be done in CI/CD & SCM

* dedicated runner, cached for requirements, version and data, queue system in place for multiple test runs, idle timeout of VMs to ensure there is not cost when tests are not running.
* CML report generation
* Configure no commit branches
* PR template
* After everything is in place create a github repository template from the exist repository
* Setup pre-commit hook
* Setup make files
* Conventional commit
* SemVer
* Validate change log generation
* formatting, linting in CI
* Running static code analysis in CI (Sonar Cloud, Bandit, mypy, flake8, pylint etc.)
* Run tests in cloud and generate coverage report.
* Publish coverage report to sonar cloud
* Build and push docker images
* Scan docker images using snyk
* Publish library to a private repository
* For pull request and push send notification to discord and MS teams.