/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.2
import QtQuick.Controls 6.2
import UntitledProject

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Button {
        id: button
        text: "Scan"
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: -194
        anchors.horizontalCenterOffset: 38
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter

        Connections {
            target: button
            onClicked: animation.start()
        }
    }

    TextInput {
        id: textInput
        x: 39
        y: 25
        width: 249
        height: 41
        text: qsTr("New Search")
        font.pixelSize: 22
    }

    Button {
        id: button1
        text: "Reports "
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenterOffset: 144
        Connections {
            target: button1
            onClicked: animation.start()
        }
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenterOffset: -195
    }

    Button {
        id: button2
        text: "About Us"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenterOffset: 250
        Connections {
            target: button2
            onClicked: animation.start()
        }
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenterOffset: -194
    }
    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:4}D{i:6}
}
##^##*/
