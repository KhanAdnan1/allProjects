import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ForgotPassword extends StatefulWidget {
  const ForgotPassword({super.key});

  @override
  State<ForgotPassword> createState() => _ForgotPassword();
}

class _ForgotPassword extends State<ForgotPassword> {
  final TextEditingController _userId = TextEditingController();
  final TextEditingController _newPassword = TextEditingController();
  final TextEditingController _reenterPassword = TextEditingController();
  Future<void> _forgetPassword() async {
    final user = _userId.text;
    final password = _reenterPassword.text;
    final newPassword = _newPassword.text;
    final reenterPassword = _reenterPassword.text;

    if (newPassword != reenterPassword) {
      // Passwords do not match
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text(' Passwords do not match '),
            actions: <Widget>[
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
      return; // Return early if passwords do not match
    }

    final response = await http.post(
      Uri.parse('https://newclgsercer.onrender.com/forgotpassword'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'user': user, 'password': password}),
    );

    final data = jsonDecode(response.body);

    if (response.statusCode == 200) {
      // Password change successful
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Success'),
            content: Text('Password changed successfully'),
            actions: <Widget>[
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    } else {
      // User not found or other error
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text(data['error']),
            actions: <Widget>[
              TextButton(
                onPressed: () {
                  Navigator.of(context).pop();
                },
                child: Text('OK'),
              ),
            ],
          );
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(children: [
        Column(
          children: [
            Container(
              height: (MediaQuery.of(context).size.height * 1),
              decoration: BoxDecoration(
                  gradient: new LinearGradient(
                      colors: [Colors.blue.shade200, Colors.blue.shade300])),
              child: Container(
                margin: EdgeInsets.only(
                    top: (MediaQuery.of(context).size.height * 0.15)),
                decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.only(
                        topLeft: Radius.circular(35),
                        topRight: Radius.circular(35))),
                child: ListView(
                  children: [
                    Text('Forgot Password',
                        style: TextStyle(
                            fontSize: 25, fontWeight: FontWeight.bold),
                        textAlign: TextAlign.center),
                    SizedBox(
                        height: (MediaQuery.of(context).size.height * 0.02)),
                    Center(
                      child: Container(
                        height: 1,
                        width: (MediaQuery.of(context).size.width * 0.9),
                        color: Colors.grey,
                      ),
                    ),
                    SizedBox(
                      height: (MediaQuery.of(context).size.height * 0.05),
                    ),
                    Container(
                      margin: EdgeInsets.symmetric(horizontal: 15),
                      child: TextField(
                        controller: _userId,
                        textAlign: TextAlign.center,
                        keyboardType: TextInputType.text,
                        decoration: InputDecoration(
                          hintText: 'User Id',
                          hintStyle: TextStyle(
                              fontWeight: FontWeight.bold, letterSpacing: 1.0),
                          border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(20),
                              borderSide: BorderSide(
                                  width: 0,
                                  style: BorderStyle.solid,
                                  color: Colors.blue)),
                          filled: true,
                          fillColor: Colors.grey[200],
                          contentPadding: EdgeInsets.all(12),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: (MediaQuery.of(context).size.height * 0.05),
                    ),
                    Container(
                      margin: EdgeInsets.symmetric(horizontal: 15),
                      child: TextField(
                        controller: _newPassword,
                        textAlign: TextAlign.center,
                        keyboardType: TextInputType.text,
                        decoration: InputDecoration(
                          hintText: 'New Password',
                          hintStyle: TextStyle(
                              fontWeight: FontWeight.bold, letterSpacing: 1.0),
                          border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(20),
                              borderSide: BorderSide(
                                  width: 0,
                                  style: BorderStyle.solid,
                                  color: Colors.blue)),
                          filled: true,
                          fillColor: Colors.grey[200],
                          contentPadding: EdgeInsets.all(12),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: (MediaQuery.of(context).size.height * 0.05),
                    ),
                    Container(
                      margin: EdgeInsets.symmetric(horizontal: 15),
                      child: TextField(
                        controller: _reenterPassword,
                        textAlign: TextAlign.center,
                        keyboardType: TextInputType.text,
                        decoration: InputDecoration(
                          hintText: 'Reenter Password',
                          hintStyle: TextStyle(
                              fontWeight: FontWeight.bold, letterSpacing: 1.0),
                          border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(20),
                              borderSide: BorderSide(
                                  width: 0,
                                  style: BorderStyle.solid,
                                  color: Colors.blue)),
                          filled: true,
                          fillColor: Colors.grey[200],
                          contentPadding: EdgeInsets.all(12),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: (MediaQuery.of(context).size.height * 0.05),
                    ),
                    Container(
                        margin: EdgeInsets.symmetric(horizontal: 15),
                        child: ElevatedButton(
                            style: ElevatedButton.styleFrom(
                                primary: Colors.blue,
                                shape: RoundedRectangleBorder(
                                    side: BorderSide(width: 0.1),
                                    borderRadius: BorderRadius.circular(20))),
                            onPressed: _forgetPassword,
                            child: Text(
                              'Resset Password',
                              style: TextStyle(
                                  fontSize: 20,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white),
                            )))
                  ],
                ),
              ),
            ),
          ],
        ),
      ]),
    );
  }
}
