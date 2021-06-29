# open_source_info_env_public
A public repository for open source information environment analysis on low resource countries.

This public repository includes files associated with research conducted to explore and evaluate the open source information environment for low-resource countries, using Niger as a case study.

There are three main avenues of reserach included.

First, twitter_usage is a series of python ipynb code files that uses publicly available archive.org "spritzer" tweet data.  Provided the user downloads and unzips this data, these files will filter them for place- or coordinate- tagged tweets, compute basic statistics about them, and then allow plotting and visualization of tweet volume by countries, coontinents, timezones, or on an interactive map.  The program manages memory along the way allowing computations of significant sized datasets of the programmer's choosing.

Second, twitter_scraping uses the popular Twint library to scrape Twitter data, one year at a time, for a populated area.  By definition, the results will be geographically associated with that area.  The scripts then filter and plot the data to allow the user to visualize long term trends and draw generalized inferences about the twitter volume for a particular low resource country.  This version is currently set up to evaluate several major population areas of Niger.  Some sample scraped data is included in csv files.

Finally, the radio_stream set of files provides a set of scripts and tools that can be used for initial recording of sound segments from publicly-facing internet-based radio streams that are based in, discuss, or may relate to the case study country of Niger.  The tools include recording segments of radio, sending those recordings for Google Cloud Speech to Text and Google Cloud Translate, splitting audio files, and other audio processing that may aid in preparing the files for coud-based of Kaldi-based Automated Speech Recognition (ASR) programs. 


