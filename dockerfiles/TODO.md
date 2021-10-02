Here we need to have different type of docker files which can be used for different purpose such as,

* __Base image for library:__ lightweight, no cache, multi-stage, no addition system dependency, and binary files
* __Job Runner image:__ Base image with entry point script as runner for CLI app. It should be able to take command line arguments.
* __Development env image:__ Base library along with jupyter and other dependencies installed and endpoint as jupyter notebook.
* __Test env image:__ This test image can be build on top of the base library image. All the test dependency and basic requirements can be mounted here.