# Job runner image

The only difference of this image from the supervisord image is that this image will run the script and will terminal the job. So, it will not keep running the script once the job is done. The other files remain same as the `with_supervisord` directory.

* __Note:__ Here also, one has to create `*.whl` file first and put that in the same directory where the `Dockerfile` is located. Replace the name of the library in the two places in `Dockerfile`. Change the `runner.py` file as per requirement. Once this is done, build and test the image. 