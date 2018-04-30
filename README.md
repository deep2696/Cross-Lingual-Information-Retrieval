# Cross Lingual Information Retrieval

This project proposes a Devanagari to Roman script (and vice versa) transliteration system targeting old Sanskrit documents and manuscripts. This system first transliterates a given query term containing Roman characters into Devanagari script, which will later be used to retrieve documents relevant to the transliterated and the original query. It also converts a document given in Devanagari script to Roman script.


### Prerequisites


```
keras
tensorflow==1.4

```

### Installing


```
pip install -r requirements.txt
```

or

```
pip install keras
pip install tensorflow
pip install matplotlib
pip install indic_transliteration

```
### Example


```
Input:-
श्रीपार्वतीसुकुचकुङ्कुमराजमानवक्षःस्थलाञ्चितममेयगुणप्रपञ्चम् ।
वन्दारुभक्तजनमङ्गलदायकं तं वन्दे सदाशिवमहं वरदं महेशम् ॥ १.१॥

Output:-
shriparvatisukucakugkumarajamanavaksahsthalajcitamameyagunaprapajcam |
vandarubhaktajanamaggaladayakam tam vande sadashivamaham varadam mahesham || 1.1||


Input:-
narayanam om namah shivaya karmay uvach drishta tu pandava nikam karan uvachaya|
namami cha drishta tu bhagwan uvach |
drishta tu pandaw ||

Output:-
नारायणं ओं नमः शिवाय कर्माय उवाच दृष्टा तु पाण्डव निकं करन् उवाचया |
नमामि च दृष्टा तु भागण उवाच |
दृष्टा तु पाण्डा ||
```



## Authors

* **Sujal Maheswari** - [IIT-Sujal](https://github.com/IIT-Sujal)
* **Deepanshu Gupta** - [deep2696](https://github.com/deep2696)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
