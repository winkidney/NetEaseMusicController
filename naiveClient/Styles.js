'use strict';

var React = require('react-native');
var {
  StyleSheet,
  } = React;

export const styles = StyleSheet.create({
  scrollView: {
    flex: 1,
  },
  container: {
    flex: 1,
    alignItems: 'stretch',
    backgroundColor: '#F5FCFF',
    padding: 20,
  },
  row: {
    flexDirection: 'row',
    marginVertical: 10,
  },
  textLine: {
  	flexDirection: 'row',
  },
  col: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    marginLeft: 7, marginRight: 7,
  },
  colNoAlign: {
    flex: 1,
    flexDirection: 'column',
    marginLeft: 7, marginRight: 7,
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  controllerButton: {
    flex: 1,
    marginHorizontal: 20,
    width: 120,
  },
  fab: {
    // width: 200,
    // height: 200,
    // borderRadius: 100,
  },
  textfieldWithFloatingLabel: {
    height: 38,
  },
  buttonText: {
    fontSize: 14,
    fontWeight: 'bold',
    color: 'white',
  },
  playPauseButton: {
    flex: 1,
    marginHorizontal: 20,
    width: 240,
    height: 50,
  },
  connectedMarker: {
    color: 'green',
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  }
});