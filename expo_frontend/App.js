import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, SafeAreaView, TextInput, Alert } from 'react-native';
import { WebView } from 'react-native-webview';
import Constants from 'expo-constants';

export default function App() {
  // Replace 192.168.1.100 with your computer's actual IP address
  const [serverUrl, setServerUrl] = useState('http://192.168.0.104:5000/');
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    // Test connection when component mounts
    checkServerConnection();
  }, []);

  const checkServerConnection = async () => {
    try {
      const response = await fetch(serverUrl);
      if (response.ok) {
        setIsConnected(true);
      } else {
        Alert.alert('Connection Error', 'Could not connect to server');
      }
    } catch (error) {
      Alert.alert('Connection Error', 'Could not connect to server: ' + error.message);
    }
  };

  if (!isConnected) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.header}>
          <Text style={styles.title}>Hand Detection Game</Text>
          <Text style={styles.subtitle}>Connecting to server...</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Hand Detection Game</Text>
      </View>
      <View style={styles.webviewContainer}>
        <WebView
          source={{ uri: serverUrl }}
          style={styles.webview}
          javaScriptEnabled={true}
          domStorageEnabled={true}
          startInLoadingState={true}
          mixedContentMode="always"
          allowsInlineMediaPlayback={true}
          mediaPlaybackRequiresUserAction={false}
          onError={(syntheticEvent) => {
            const { nativeEvent } = syntheticEvent;
            console.warn('WebView error: ', nativeEvent);
            Alert.alert('WebView Error', 'Failed to load content');
          }}
          onHttpError={(syntheticEvent) => {
            const { nativeEvent } = syntheticEvent;
            console.warn('HTTP error: ', nativeEvent);
            Alert.alert('Connection Error', `HTTP Error: ${nativeEvent.statusCode}`);
          }}
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a202c',
    paddingTop: Constants.statusBarHeight,
  },
  header: {
    padding: 15,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
  subtitle: {
    fontSize: 16,
    color: '#a0aec0',
    marginTop: 8,
  },
  webviewContainer: {
    flex: 1,
    overflow: 'hidden',
    borderRadius: 10,
    margin: 10,
  },
  webview: {
    flex: 1,
    backgroundColor: 'transparent',
  },
});