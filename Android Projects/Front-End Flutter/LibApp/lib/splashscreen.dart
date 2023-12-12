import 'dart:async';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'login.dart';
import 'navigation.dart';

class SplashScreen extends StatefulWidget {
  @override
  State<SplashScreen> createState() => SplashScreenState();
}

class SplashScreenState extends State<SplashScreen> {
  static const String KEYLOGIN = 'Login';

  @override
  void initState() {
    super.initState();
    whereToGo();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      decoration: BoxDecoration(
          gradient: new LinearGradient(
              colors: [Colors.blue.shade200, Colors.blue.shade300])),
      child: Center(
        child: Text(
          'Digital Library',
          style: TextStyle(
              fontWeight: FontWeight.bold, fontSize: 30, color: Colors.white),
        ),
      ),
    ));
  }

  void whereToGo() async {
    var shsredPreferences = await SharedPreferences.getInstance();
    var stuName = shsredPreferences.getString('stuName'); // Fetch stuName
    var className = shsredPreferences.getString('className'); // Fetch className

    var isLoggedin = shsredPreferences.getBool(KEYLOGIN);

    Timer(Duration(seconds: 2), () {
      if (isLoggedin != null) {
        if (isLoggedin) {
          Navigator.pushReplacement(
              context,
              MaterialPageRoute(
                  builder: (context) => Navigators.withData(
                        className: className ?? '',
                        stuName: stuName ?? '',
                      )));
        } else {
          Navigator.pushReplacement(
              context, MaterialPageRoute(builder: (context) => Login()));
        }
      } else {
        Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => Login()));
      }
    });
  }
}
