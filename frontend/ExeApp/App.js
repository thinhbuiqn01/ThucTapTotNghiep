import * as React from 'react';
import { View, Text, Image } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Signin from './src/pages/Signin';
import Signup from './src/pages/Signup';
import Home from './src/pages/Home';
import Profile from './src/pages/Profile';
import Search from './src/pages/Search';
import Room from './src/pages/Room';
import Icon from 'react-native-vector-icons/Ionicons'

const Tab = createBottomTabNavigator();

function MyTabs() {
  return (
    <Tab.Navigator screenOptions={{headerShown: false}}>
      <Tab.Screen name="Home" component={Home} 
      options={{tabBarIcon:() =>{<Icon name="heart-outline" size={30} color='#000000'/>}}}/>
      <Tab.Screen name="Search" component={Search}
      options={{tabBarIcon:() =>{<Icon name="heart-outline" size={30} color='#000000'/>}}}/>
      <Tab.Screen name="Room" component={Room}
      options={{tabBarIcon:() =>{<Icon name="heart-outline" size={30} color='#000000'/>}}}/>
      <Tab.Screen name="Profile" component={Profile}
      options={{tabBarIcon:() =>{<Icon name="heart-outline" size={30} color='#000000'/>}}}/>
    </Tab.Navigator>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer >
      <Stack.Navigator screenOptions={{headerShown: false}}>
        <Stack.Screen name="Signin" component={Signin} /> 
        <Stack.Screen name="Signup" component={Signup} />
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="HomeTabs" component={MyTabs} />

      </Stack.Navigator>
    </NavigationContainer>
  );
}



export default App;