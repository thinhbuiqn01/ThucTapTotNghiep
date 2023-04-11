import { View, Text, Button, TouchableOpacity, StyleSheet, Image, ScrollView, Modal } from 'react-native'
import React from 'react'
import Icon from 'react-native-vector-icons/Ionicons'

export default function Home ({ navigation })  {
  
  return (
    <View style={styles.container}>

      <View style={{flex:1, flexDirection:'row', marginTop:10}}>
            <Icon name="arrow-redo-outline" size={30} color='black' style={{
                marginLeft:140
            }}/>
            <Icon name="heart-outline" size={30} color='black' style={{
                marginLeft:20
            }}/>
            <TouchableOpacity>
                <Image source={{uri:'https://i.pinimg.com/originals/76/5e/1a/765e1af4ea428422b658d004be5d1362.png'}}
                     style={{
                     width: 30,
                     height: 30,
                     borderRadius:100,
                     marginLeft: 20
                }} />
            </TouchableOpacity>
            <Icon name="cart-outline" size={30} color='black' style={{
                marginLeft:20
            }}/>
            <Icon name="notifications-outline" size={30} color='black' style={{
                marginLeft:20
            }}/>
      </View>
          
      <View style={styles.coverimage}>
       <Image source={{uri:'https://cdn.tgdd.vn/Files/2022/08/12/1455652/hoa-hong-phan-y-nghia-cach-trong-va-cach-cham-soc-chi-tiet-202208120828249307.jpg'}}
                     style={{
                     width: '90%',
                     height: 170,
                     borderRadius:20,
                     marginLeft:'5%'
                }} />
        <Image source={{uri:'https://images2.thanhnien.vn/Uploaded/trucdl/2021_12_30/moneycualisalapkyluc3-8661.png'}}
                     style={{
                     width: 80,
                     height: 80,
                     borderRadius:100,
                     bottom: 100,
                     left: 40, 
                }} />
      </View>
      <View style={styles.info}>
        <View style={{alignItems:'center'}}>
          <Text style={{fontSize: 25, color:'black', fontWeight:'bold'}}>1</Text>
          <Text style={{color:'black'}}>Posts</Text>
        </View>
        <View style={{alignItems:'center'}}>
          <Text style={{fontSize: 25, color:'black', fontWeight:'bold'}}>4</Text>
          <Text style={{color:'black'}}>Followers</Text>
        </View>
        <View style={{alignItems:'center'}}>
          <Text style={{fontSize: 25, color:'black', fontWeight:'bold'}}>5</Text>
          <Text style={{color:'black'}}>Following</Text>
        </View>
        <View style={{alignItems:'center', justifyContent:'center' }}>
          <TouchableOpacity>
            <View style={styles.button}>
              <Text style={{color:'white'}}>Following</Text>
            </View>
          </TouchableOpacity>
        </View>
      </View>

      <View style={styles.postings}>
        <ScrollView>
        <View style={styles.imgs}>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        </View>
        <View style={styles.imgs}>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        </View>
        <View style={styles.imgs}>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        <Image source={require('../assets/hoa.jpg')} style={styles.img}/>
        </View>
        </ScrollView>
        <TouchableOpacity style={styles.add}>
          <Text style={{fontSize:50, color:'black'}}>+</Text>
        </TouchableOpacity>
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  coverimage:{
    flex: 5,
    position: 'relative',
  },
  info:{
    flex: 2,
    flexDirection:'row',
    justifyContent: 'space-between',
    width: '80%',
    marginLeft:'10%'
  },
  postings:{
    flex: 10
  },
  button:{
    alignItems:'center',
    justifyContent: 'center',
    backgroundColor:'#EF07BA',
    height: 30,
    width: 80,
    borderRadius:10,
    marginBottom: 20
  },
  imgs:{
    flexDirection:'row',
    justifyContent:'space-between',
    marginHorizontal: '7%',
    marginBottom:30
    

  },
  img:{
    width:150, 
    height:200,
    borderRadius: 15,
  },
  add:{
    width:80,
    height:80,
    justifyContent:'center',
    alignItems: 'center',
    position: 'absolute',
    backgroundColor:'#F1069Ck',
    top: 300,
    left: 280,
    borderRadius:100

  }

})