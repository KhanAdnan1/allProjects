import 'dart:convert';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:marquee_text/marquee_text.dart';

class Home extends StatefulWidget {
  @override
  _Home createState() => _Home();
}

class _Home extends State<Home> {
  String greeting() {
    var hour = DateTime.now().hour;
    if (hour < 12) {
      return 'Good Morning';
    }
    if (hour < 17) {
      return 'Good Afternoon';
    }
    return 'Good Evening';
  }

  //String error='Failed To return';
  List<String> imageBase64Data = []; // Store the base64 image data
  @override
  void initState() {
    super.initState();
    // Fetch image base64 data from your server's /images endpoint
    fetchImageBase64Data();
  }

  void fetchImageBase64Data() async {
    try {
      // Make the HTTP GET request to your server
      final response =
          await http.get(Uri.parse('https://newclgsercer.onrender.com/images'));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        final fetchedImages = data['data'];

        setState(() {
          imageBase64Data = fetchedImages
              .map<String>((imageData) => imageData['img'].toString())
              .toList();
        });
      }
    } catch (error) {}
  }

  Future<List<String>> fetchNoticeData() async {
    final response =
        await http.get(Uri.parse('https://newclgsercer.onrender.com/notices'));

    if (response.statusCode == 200) {
      final data = json.decode(response.body) as List<dynamic>;

      // Extract the "notices" field from each item in the list and convert it to a List<String>.
      final noticeList =
          data.map((item) => item['notices'].toString()).toList();

      return noticeList;
    } else {
      throw Exception('Failed to load notice data');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          title: Text("${greeting()}"),
          flexibleSpace: Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.centerLeft,
                end: Alignment.centerRight,
                stops: [0.0, 0.9],
                colors: [Colors.blue, Colors.white],
              ),
            ),
          ),
        ),
        body: ListView(
          children: [
            Container(
                padding: EdgeInsets.only(
                    top: (MediaQuery.of(context).size.width / 50)),
                margin: EdgeInsets.only(
                    top: (MediaQuery.of(context).size.width / 10),
                    right: (MediaQuery.of(context).size.width / 50),
                    left: (MediaQuery.of(context).size.width / 50)),
                height: (MediaQuery.of(context).size.height * 0.1),
                width: (MediaQuery.of(context).size.width * 0.55),
                child: Card(
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.only(
                        topRight: Radius.circular(15),
                        topLeft: Radius.circular(15),
                      ),
                    ),
                    elevation: 8,
                    shadowColor: Colors.lightBlue.withOpacity(0.5),
                    child: Padding(
                      padding: const EdgeInsets.only(top: 15),
                      child: Column(
                        children: [
                          Text("Welcome to  Libraray",
                              style: TextStyle(
                                  fontSize: 25,
                                  color: Colors.black,
                                  fontWeight: FontWeight.bold)),
                        ],
                      ),
                    ))),

            Container(
              margin: EdgeInsets.only(
                  top: (MediaQuery.of(context).size.height / 25),
                  right: ((MediaQuery.of(context).size.width / 50)),
                  left: (MediaQuery.of(context).size.width / 50)),
              child: Card(
                  elevation: 8,
                  shadowColor: Colors.blue,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: <Widget>[
                      CarouselSlider(
                        items: imageBase64Data.map((base64Data) {
                          final bytes =
                              base64Decode(base64Data.split(',').last);
                          return Container(
                            child: Card(
                              elevation: 8,
                              shadowColor: Colors.blue,
                              child: Image.memory(
                                  width: (MediaQuery.of(context).size.height /
                                      0.9), // Increase the width as needed
                                  height: (MediaQuery.of(context).size.height /
                                      0.9),
                                  bytes,
                                  fit: BoxFit.contain),
                            ),
                          );
                          //);
                        }).toList(),
                        options: CarouselOptions(
                          // Customize carousel options as needed
                          height: 200, // Adjust the height as needed
                          aspectRatio:
                              0 / 0, // Adjust the aspect ratio as needed
                          viewportFraction: 0.8,
                          enableInfiniteScroll: true,
                          autoPlay: true,
                        ),
                      ),
                    ],
                  )),
            ),

            //Notice...................................................

            Container(
              margin: EdgeInsets.only(
                top: (MediaQuery.of(context).size.height / 25),
                right: ((MediaQuery.of(context).size.width / 50)),
                left: (MediaQuery.of(context).size.width / 50),
                bottom: (MediaQuery.of(context).size.height / 50),
              ),
              height: (MediaQuery.of(context).size.height * 0.5),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(50),
                  topRight: Radius.circular(50),
                ),
              ),
              child: Card(
                elevation: 8,
                shadowColor: Colors.blue,
                child: Column(
                  children: [
                    Card(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.only(
                          topRight: Radius.circular(15),
                          topLeft: Radius.circular(15),
                        ),
                      ),
                      child: Container(
                        width: (MediaQuery.of(context).size.height / 0.9),
                        decoration: BoxDecoration(
                          color: Colors.blue,
                          borderRadius: BorderRadius.only(
                            topLeft: Radius.circular(18),
                            topRight: Radius.circular(18),
                          ),
                        ),
                        child: Container(
                          margin: EdgeInsets.only(left: 130),
                          child: Text(
                            "Notice",
                            style: TextStyle(
                              fontSize: 25,
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                      ),
                    ),
                    FutureBuilder<List<String>>(
                      future: fetchNoticeData(),
                      builder: (context, snapshot) {
                        if (snapshot.connectionState ==
                            ConnectionState.waiting) {
                          return CircularProgressIndicator(); // Show a loading indicator while waiting for data.
                        } else if (snapshot.hasError) {
                          return Container(
                            margin: EdgeInsets.only(top: 80),
                            child: Text('Check your internet connection ',
                                style: TextStyle(
                                    fontSize: 20,
                                    color: Colors.red,
                                    fontWeight: FontWeight.bold)),
                          );
                          // Handle errors here.
                        } else {
                          final noticeList = snapshot.data ?? [];
                          if (noticeList.isEmpty) {
                            return Container(
                              margin: EdgeInsets.only(top: 80),
                              child: Text('There is no notice',
                                  style: TextStyle(
                                      fontSize: 25,
                                      color: Colors.red,
                                      fontWeight: FontWeight.bold)),
                            );
                            // Display a message when there are no notices.
                          }
                          return Card(
                            elevation: 3,
                            shadowColor: Colors.blue,
                            child: Column(
                              children: [
                                Column(
                                  children: noticeList.map((notice) {
                                    return Container(
                                        width: (MediaQuery.of(context)
                                                .size
                                                .height /
                                            0.9),
                                        padding: EdgeInsets.all(5),
                                        child: Card(
                                          elevation: 3,
                                          shadowColor: Colors.blue,
                                          child: MarqueeText(
                                            text: TextSpan(
                                                text: notice,
                                                style: TextStyle(
                                                    fontSize: 20,
                                                    color: Colors.red,
                                                    fontWeight:
                                                        FontWeight.bold)),
                                          ),
                                        ));
                                  }).toList(),
                                ),
                              ],
                            ),
                          );
                        }
                      },
                    )
                  ],
                ),
              ),
            )

            //................................................................Notice
          ],
        ));
  }
}
