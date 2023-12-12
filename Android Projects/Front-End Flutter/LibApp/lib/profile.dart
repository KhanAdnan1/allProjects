import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import './forgotPass.dart';
import './login.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Profile extends StatefulWidget {
  final String stuName;
  final String className;

  const Profile({
    Key? key,
    required this.stuName,
    required this.className,
  }) : super(key: key);

  @override
  _Profile createState() => _Profile();
}

class _Profile extends State<Profile> {
  static const String KEYLOGIN = 'Login';
  void _loginSuccessful() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setBool(KEYLOGIN, true);
    // Other data you want to store, e.g., stuName, className, etc.
  }

  File? _image;
  Color textColor = Colors.black;
  Color cardColor = Colors.white;
  Color cardColor2 = Colors.white;

  Future<void> _pickImage() async {
    final imagePicker = ImagePicker();
    final pickedImage =
        await imagePicker.pickImage(source: ImageSource.gallery);

    if (pickedImage != null) {
      final imageBytes = await pickedImage.readAsBytes();
      final base64Image = base64Encode(imageBytes);

      SharedPreferences prefs = await SharedPreferences.getInstance();
      prefs.setString('user_image', base64Image);

      setState(() {
        _image = File(pickedImage.path);
      });
    }
  }

  @override
  void initState() {
    super.initState();
    _loadImageFromPreferences();
  }

  _loadImageFromPreferences() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String? base64Image = prefs.getString('user_image');

    if (base64Image != null) {
      try {
        Uint8List uint8List = base64Decode(base64Image);
        if (uint8List.isNotEmpty) {
          setState(() {
            // Create a temporary file to store the image data
            _image = File('${Directory.systemTemp.path}/temp_image.png');
            _image!.writeAsBytesSync(
                uint8List); // Write the image data to the file
          });
        } else {
          print("Base64 image data is empty.");
        }
      } catch (error) {
        print("Error decoding base64 image: $error");
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Profile'),
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
              margin: EdgeInsets.only(top: 50),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  _image != null
                      ? CircleAvatar(
                          radius: 60,
                          backgroundImage: FileImage(_image!),
                        )
                      : CircleAvatar(
                          radius: 60,
                          child: Icon(Icons.person, size: 60),
                        ),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: _pickImage,
                    child: Text('Pick Photo'),
                  ),
                ],
              ),
            ),
            Column(
              children: [
                Container(
                  height: 75,
                  width: 350,
                  margin: EdgeInsets.only(
                      top: (MediaQuery.of(context).size.width / 50)),
                  child: Card(
                      elevation: 8,
                      child: Container(
                        margin: EdgeInsets.only(
                            left: (MediaQuery.of(context).size.width / 8),
                            top: (MediaQuery.of(context).size.width / 15)),
                        child: Text('Class: ' + widget.className,
                            style: TextStyle(
                                fontSize: 20, fontWeight: FontWeight.w700)),
                      )),
                ),
                Container(
                  height: 75,
                  width: 350,
                  margin: EdgeInsets.only(
                      top: (MediaQuery.of(context).size.width / 50)),
                  // decoration: BoxDecoration(
                  //   color: Colors.yellow,
                  // ),
                  child: Card(
                      elevation: 8,
                      child: Container(
                        margin: EdgeInsets.only(
                            left: (MediaQuery.of(context).size.width / 8),
                            top: (MediaQuery.of(context).size.width / 15)),
                        child: Text('Name: ' + widget.stuName,
                            style: TextStyle(
                                fontSize: 20, fontWeight: FontWeight.w600)),
                      )),
                ),
                Container(
                  height: 75,
                  width: 350,
                  margin: EdgeInsets.only(
                      top: (MediaQuery.of(context).size.width / 50)),
                  child: Card(
                      elevation: 8,
                      color: cardColor,
                      child: Container(
                          margin: EdgeInsets.only(
                              left: (MediaQuery.of(context).size.width / 8),
                              top: (MediaQuery.of(context).size.width / 15)),
                          child: InkWell(
                            onTap: () {
                              setState(() {
                                textColor = Colors
                                    .white; // Change to your desired color
                                cardColor = Colors.blue;
                              });
                              Navigator.pop(context);
                              Navigator.of(context).push(MaterialPageRoute(
                                  builder: (context) => ForgotPassword()));
                            },
                            child: Container(
                              child: Text('Change Password',
                                  style: TextStyle(
                                      fontSize: 20,
                                      color: textColor,
                                      fontWeight: FontWeight.w500)),
                            ),
                          ))),
                ),
                Container(
                  height: 75,
                  width: 350,
                  margin: EdgeInsets.only(
                      top: (MediaQuery.of(context).size.width / 50)),
                  child: Card(
                      elevation: 8,
                      color: cardColor2,
                      child: Container(
                          margin: EdgeInsets.only(
                              left: (MediaQuery.of(context).size.width / 8),
                              top: (MediaQuery.of(context).size.width / 15)),
                          child: InkWell(
                            onTap: () async {
                              setState(() {
                                textColor = Colors
                                    .white; // Change to your desired color
                                cardColor2 = Colors.redAccent;
                              });
                              SharedPreferences prefer =
                                  await SharedPreferences.getInstance();
                              prefer.setBool(KEYLOGIN, false);

                              Navigator.pop(context);
                              Navigator.of(context).push(MaterialPageRoute(
                                  builder: (context) => Login()));
                            },
                            child: Container(
                              child: Text('Log Out',
                                  style: TextStyle(
                                      fontSize: 20,
                                      color: textColor,
                                      fontWeight: FontWeight.w400)),
                            ),
                          ))),
                )
              ],
            )
          ],
        ));
  }
}
