import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class TextInput extends StatelessWidget {
  TextInput({
    super.key,
    this.keyboardType,
    this.maxLength,
    required this.onSave,
    this.validate,
  });

  TextInputType? keyboardType = TextInputType.text;
  int? maxLength = 50;
  void Function(String?) onSave;
  String? Function(String?)? validate;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        children: [
          const Text(
            "How much time do you have?",
            // style: TextStyle(color: Colors.white),
          ),
          TextFormField(
              validator: validate,
              onSaved: onSave,
              keyboardType: TextInputType.text,
              maxLength: maxLength,
              style:
                  TextStyle(color: Theme.of(context).scaffoldBackgroundColor),
              decoration: InputDecoration(
                filled: true,
                fillColor: Colors.white,
                errorBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(50),
                  borderSide: const BorderSide(
                      color: Color.fromARGB(255, 188, 34, 23), width: 3.0),
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(50),
                  borderSide: BorderSide(
                      color: Theme.of(context).primaryColor, width: 3.0),
                ),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(50),
                ),
              ))
        ],
      ),
    );
  }
}
