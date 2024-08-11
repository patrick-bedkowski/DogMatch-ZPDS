import 'package:flutter/material.dart';

class ShowDogPage extends StatelessWidget {
  const ShowDogPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("German Shepherd"),
        ),
        body: Text("nice dog"));
  }
}
