import 'dart:async';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_pdfview/flutter_pdfview.dart';

class NovelsView extends StatefulWidget {
  final Uint8List novelPdfData;
  final String contentType;
  final String title;

  const NovelsView({
    Key? key,
    required this.novelPdfData,
    required this.contentType,
    required this.title,
  }) : super(key: key);

  @override
  _NovelsViewState createState() => _NovelsViewState();
}

class _NovelsViewState extends State<NovelsView> {
  final Completer<PDFViewController> _controller =
      Completer<PDFViewController>();
  int? totalPages = 0;
  bool isReady = false;
  int? currentPage = 0;
  String errorMessage = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Stack(
        children: [
          PDFView(
            pdfData: widget.novelPdfData,
            enableSwipe: true,
            autoSpacing: true,
            onRender: (_pages) {
              setState(() {
                totalPages = _pages;
                isReady = true;
              });
            },
            onPageChanged: (int? page, int? total) {
              setState(() {
                currentPage = page;
              });
            },
            onViewCreated: (PDFViewController pdfViewController) {
              _controller.complete(pdfViewController);
            },
          ),
          errorMessage.isEmpty
              ? !isReady
                  ? Center(
                      child: CircularProgressIndicator(),
                    )
                  : Container()
              : Center(
                  child: Text(errorMessage),
                ),
          Positioned(
            bottom: 16.0,
            right: 16.0,
            child: Container(
              padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
              decoration: BoxDecoration(
                color: Colors.black.withOpacity(0.7),
                borderRadius: BorderRadius.circular(8.0),
              ),
              child: Text(
                'Page ${currentPage ?? 1}/$totalPages',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 16.0,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
