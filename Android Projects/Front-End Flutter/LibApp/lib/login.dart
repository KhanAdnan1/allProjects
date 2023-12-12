import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:libapp/splashscreen.dart';
import 'package:shared_preferences/shared_preferences.dart';
import './forgotPass.dart';
import './navigation.dart';

class Login extends StatefulWidget {
  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  Future<void> _login() async {
    final String username = _usernameController.text;
    final String password = _passwordController.text;
    final response = await http.post(
      Uri.parse('https://newclgsercer.onrender.com/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'user': username, 'password': password}),
    );
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      //final token = data['token'];

      final className = data['className'];
      final stuName = data['stuName'];

      var sharedPreferences = await SharedPreferences.getInstance();
      sharedPreferences.setBool(SplashScreenState.KEYLOGIN, true);
      sharedPreferences.setString('className', className); // Save className
      sharedPreferences.setString('stuName', stuName); // Save stuName

      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) =>
              Navigators.withData(className: className, stuName: stuName),
        ),
      );
    } else {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text('Invalid credentials. Please try again.'),
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
              child: ListView(children: [
                Text('Login',
                    style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
                    textAlign: TextAlign.center),
                SizedBox(height: (MediaQuery.of(context).size.height * 0.02)),
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
                    controller: _usernameController,
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
                    controller: _passwordController,
                    textAlign: TextAlign.center,
                    keyboardType: TextInputType.text,
                    decoration: InputDecoration(
                      hintText: 'Password',
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
                        onPressed: _login,
                        child: Text(
                          'Login',
                          style: TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Colors.white),
                        ))),
                SizedBox(
                  height: (MediaQuery.of(context).size.height * 0.01),
                ),
                Container(
                  margin: EdgeInsets.symmetric(horizontal: 15),
                  child: TextButton(
                      onPressed: () {
                        Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => ForgotPassword()));
                      },
                      child: Text(
                        'Forgot Password?',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      )),
                )
              ]),
            ),
          )
        ],
      )
    ]));
  }
}
