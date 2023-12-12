import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'novelsView.dart';

class Novel extends StatefulWidget {
  const Novel({super.key});
  @override
  _Novel createState() => _Novel();
}

class _Novel extends State<Novel> {
  List<Novels> Novelspdf = [];
  @override
  void initState() {
    super.initState();
    _fetchPdfBooks();
  }
  //https://newclgsercer.onrender.com/novels/pdf
  Future<void> _fetchPdfBooks() async {
    final url = 'http://192.168.128.107:5000/novels/pdf';
    //print('Fetching novels data');
    final response = await http.get(Uri.parse(url),
        headers: {'Content-Type': 'application/json; charset=utf-8'});
    //print('Response status code: ${response.statusCode}');
    if (response.statusCode == 200) {
      final List<dynamic> novelsData = jsonDecode(response.body);
      final List<Novels> novels = [];
      //print('Novels Data: $novelsData');
      for (final novelData in novelsData) {
        final title = novelData['title'];
        final pdfDataArray = novelData['novelPdfData'];
        final novelPdfData = Uint8List.fromList(List<int>.from(pdfDataArray));
        final contentType = novelData['contentType'];
        novels.add(Novels(
            title: title,
            novelPdfData: novelPdfData,
            contentType: contentType));
      }
      setState(() {
        Novelspdf = novels;
      });
    } else {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text('Failed to fetch PDF Novels.'),
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
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Novels'),
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
      body: Novelspdf.isNotEmpty
          ? ListView.builder(
              itemCount: Novelspdf.length,
              itemBuilder: (context, index) {
                final novels = Novelspdf[index];
                return Card(
                  margin: EdgeInsets.all(8.0),
                  elevation: 15,
                  shadowColor: Colors.blue,
                  color: Colors.blue.shade300,
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0)),
                  child: ListTile(
                    title: Text(novels.title,
                        style: TextStyle(
                            color: Colors.white,
                            fontSize: 18.0,
                            fontWeight: FontWeight.bold)),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => NovelsView(
                              novelPdfData: novels.novelPdfData,
                              contentType: novels.contentType,
                              title: novels.title),
                        ),
                      );
                    },
                  ),
                );
              },
            )
          : Center(child: CircularProgressIndicator()),
    );
  }
}

class Novels {
  final String title;
  final Uint8List novelPdfData;
  final String contentType;
  Novels(
      {required this.title,
      required this.novelPdfData,
      required this.contentType});
}
