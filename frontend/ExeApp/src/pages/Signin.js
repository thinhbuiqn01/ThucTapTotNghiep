import { StyleSheet, Text, View, TouchableOpacity, Button, ImageBackground, TextInput } from 'react-native'
import axios from 'axios';
import React, { useState, useEffect } from 'react';

export default function Signin({navigation}) {


  const [name, setname] = useState('');
  const [password, setPassword] = useState('');
  const dataUser = {
    name: name,
    password: password,
  };

  const Submit = () => {
    try {
      const res = axios
        .post('http://10.0.2.2:8000/api/login', dataUser)
        .then(response => {
          // handle the response data
          console.log(response.data);
          if (response.data.status === 200) {
            console.log(response.data.message);
            navigation.replace('HomeTabs');
          } else {
            console.log(response.data.message);
          }
        })
        .catch(error => {
          // handle the error
          console.log(error);
        });
      } catch (e) {
        console.log('Error', e.message);
      }
  };

  
  

  return (
    <View style={styles.container}>
    <ImageBackground source={require('../assets/bgr.jpg')} resizeMode="cover" style={styles.image}>
      <View style={styles.formcontainer}>
            <Text style={styles.header}>Đăng Nhập</Text>

            <View style={styles.form}>
              <Text style={styles.text}>Tên đăng nhập</Text>
              <TextInput style={styles.input} onChangeText={(text)=> setname(text)}
              />
              <Text style={styles.text}>Mật khẩu</Text>
              <TextInput style={styles.input} secureTextEntry onChangeText={(text)=> setPassword(text)}
              />
              <TouchableOpacity style={styles.btn} onPress={Submit}>
                <Text style={{color:'white', fontSize:18, fontWeight:500}}>Đăng nhập</Text>
              </TouchableOpacity>
            </View>
      </View>
      <View style={{flexDirection:'row', marginTop:4}}>
        <Text style={{color:'black', fontSize:16, fontWeight:'600'}}>Bạn đã có tài khoản? </Text>
        <TouchableOpacity onPress={()=> navigation.navigate('Signup')}>
        <Text style={{color:"#FC0400", fontSize:16, fontWeight:'600'}}>Đăng kí.</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  </View>
  )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
    },
    image: {
      flex: 1,
      justifyContent: 'center',
      alignItems:'center',
    },
    formcontainer:{
        height: 500,
        width: 300,
        backgroundColor:'white',
        borderRadius: 15,
        shadowColor: '#CAC1C8',
    shadowOffset: {
      width: 0,
      height: 5,
    },
    shadowOpacity: 0.5,
    shadowRadius: 4.11,
    elevation: 6,

    },
    header:{
        color: "#0F04F9",
        fontWeight: '500',
        fontSize: 25,
        marginTop: 30,
        marginLeft: 30,
    },
    form:{
        marginTop: 50,
    },
    text:{
        color: 'black',
        fontSize: 15,
        marginLeft: 30,
        marginBottom: 10,
        fontWeight:'400',
    },
    input:{
        height: 40,
        borderColor: "#AFAFB3",
        borderWidth: 1,
        borderRadius:30,
        marginHorizontal: 30,
        marginBottom:10,
        paddingLeft: 20
    },
    btn: {
        backgroundColor:"#9210F9",
        height:40,
        marginHorizontal: 30,
        borderRadius:30,
        alignItems:'center',
        justifyContent:'center',
        marginTop: 50
    },
  });