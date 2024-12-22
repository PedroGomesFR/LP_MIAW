import React from 'react';
import { View, Text, StyleSheet,ImageBackground } from 'react-native'; // Ensure StyleSheet is importedimport icedCoffee from "@/assets/images/coffee.jpg";

const App = () => {
  return (
    <View style={styles.container}>
        <ImageBackground
        source={icedCoffee}
        resizeMode="cover"
        style={styles.image}
        >
            <Text style={styles.text}>Coffee Shop</Text>
        </ImageBackground>
    </View>
  );
};

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column', 
    justifyContent: 'center', 
    alignItems: 'center', 
    backgroundColor: 'black', 
  }
});