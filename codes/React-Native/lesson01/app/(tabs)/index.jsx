import React from 'react';
import { View, Text, StyleSheet,ImageBackground } from 'react-native'; // Ensure StyleSheet is imported

import icedCoffee from "@/assets/images/coffee.jpg";

const App = () => {
  return (
    <View style={styles.container}>
        <ImageBackground
        source={icedCoffee}
        resizeMode="cover"
        style={styles.image}
        >
            <Text style={styles.titre}>L'application de Pedro</Text>
            <Text style={styles.text}>Coffee</Text>
        </ImageBackground>
    </View>
  );
};

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  text: {
    color: 'white', 
    fontSize: 48,
    fontWeight: 'bold',
    textAlign: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
  },
  image: {
    width: '100%', 
    height: '100%', 
    justifyContent: 'center',
  },
  titre: {
    color: 'white', 
    fontSize: 48,
    fontWeight: 'bold',
    textAlign: 'right',
    backgroundColor: 'rgba(14, 14, 0, 0)',
  }
});
