import 'package:dog_match/screens/show_dog.dart';
import 'package:flutter/material.dart';

class MyDogsPage extends StatelessWidget {
  const MyDogsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Your dogs"),
        ),
        body: Column(
          children: [
            TextButton(
                onPressed: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(
                        builder: (BuildContext context) => const ShowDogPage()),
                  );
                },
                child: Text("Dog 1")),
            TextButton(
                onPressed: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(
                        builder: (BuildContext context) => const ShowDogPage()),
                  );
                },
                child: Text("Dog 1"))
          ],
        ));
  }
}
