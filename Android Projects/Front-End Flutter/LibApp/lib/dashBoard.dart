import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'PdfView.dart';

class Dashboard extends StatefulWidget {
  final String className;
  const Dashboard({Key? key, required this.className}) : super(key: key);
  @override
  _DashboardState createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  List<Book> _pdfBooks = [];
  @override
  void initState() {
    super.initState();
    _fetchPdfBooks();
  }
  //https://newclgsercer.onrender.com/books/${widget.className}/pdf
  Future<void> _fetchPdfBooks() async {
    final url = 'http://192.168.128.107:5000/books/${widget.className}/pdf';
    print(url);
    final response = await http.get(
      Uri.parse(url),
      headers: {'Content-Type': 'application/json; charset=utf-8'},
    );

    if (response.statusCode == 200) {
      final List<dynamic> booksData = jsonDecode(response.body);
      final List<Book> books = [];
      for (final bookData in booksData) {
        final title = bookData['title'];
        final pdfDataArray = bookData['pdfData'];
        final pdfData = Uint8List.fromList(List<int>.from(pdfDataArray));
        final contentType = bookData['contentType'];
        books.add(
            Book(title: title, pdfData: pdfData, contentType: contentType));
      }
      setState(() {
        _pdfBooks = books;
      });
    } else {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text('Error'),
            content: Text('Failed to fetch PDF books.'),
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
        title: Text(widget.className),
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
      body: _pdfBooks.isNotEmpty
          ? ListView.builder(
              itemCount: _pdfBooks.length,
              itemBuilder: (context, index) {
                final book = _pdfBooks[index];
                return Card(
                  margin: EdgeInsets.all(8.0),
                  elevation: 15,
                  shadowColor: Colors.blue,
                  color: Colors.blue.shade300,
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0)),
                  child: ListTile(
                    title: Text(book.title,
                        style: TextStyle(
                            color: Colors.white,
                            fontSize: 18.0,
                            fontWeight: FontWeight.bold)),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => PDFScreen(
                              pdfData: book.pdfData,
                              contentType: book.contentType,
                              title: book.title),
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

class Book {
  final String title;
  final Uint8List pdfData;
  final String contentType;

  Book({required this.title, required this.pdfData, required this.contentType});
}
