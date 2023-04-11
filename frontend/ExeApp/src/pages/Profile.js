import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native'
import React from 'react'
import Icon from 'react-native-vector-icons/Ionicons'

export default function Profile ({navigation}) {
  return (
    <View style={styles.comtainer}>
        <View style={styles.header}>
            
            <Text style={{
                fontSize:20,
                fontWeight: 'bold',
                color: 'black',
                marginTop:2,
                marginLeft: 40
            }}>Profile</Text>
            
            <Icon name="heart-outline" size={30} color='black' style={{
                marginLeft:140
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
        </View>

        <View style={styles.avatar}>
        <TouchableOpacity>
                <Image source={{uri:'https://images2.thanhnien.vn/Uploaded/trucdl/2021_12_30/moneycualisalapkyluc3-8661.png'}}
                     style={{
                     width: 80,
                     height: 80,
                     borderRadius:100,
                     marginLeft: 20
                }} />
        </TouchableOpacity> 
        <View>
            <Text style={{
                color: 'red',
                fontSize: 25,
                marginLeft: 20,
                marginTop: 10,
            }}>Lisa</Text>
            <Text style={{
                color:'black',
                fontSize:15,
                marginTop: 5,
                marginLeft:20
            }}>lisablackpink@gmail.com</Text>
        </View>
        </View>    

        <View style={styles.contact}>
            <Text style={{
                color:'black',
                marginVertical:20,
                marginLeft:20,
            }}>Contact Details</Text>
            <View style={styles.detail1}>
            <Icon name="person-outline" size={30} color='black' style={{
                marginLeft:20,
            }}/>
            <Text style={{
                fontSize:20,
                marginLeft:30,
                color:'black'
            }}>Edit Profile</Text>
            <Icon name="chevron-forward-outline" size={20} color='black' style={{
                marginLeft: 170
            }}/>
            </View>
            <View style={styles.detail}>
            <Icon name="mail-outline" size={30} color='black' style={{
                marginLeft:20,
            }}/>
            <Text style={{
                fontSize:20,
                marginLeft:30,
                color:'black'
            }}>Email address</Text>
            <Icon name="chevron-forward-outline" size={20} color='black' style={{
                marginLeft: 140
            }}/>
            </View>
            <View style={styles.detail}>
            <Icon name="call-outline" size={30} color='black' style={{
                marginLeft:20,
            }}/>
            <Text style={{
                fontSize:20,
                marginLeft:30,
                color:'black'
            }}>Phone number</Text>
            <Icon name="chevron-forward-outline" size={20} color='black' style={{
                marginLeft: 135
            }}/>
            </View>
            <View style={styles.detail}>
            <Icon name="location-outline" size={30} color='black' style={{
                marginLeft:20,
            }}/>
            <Text style={{
                fontSize:20,
                marginLeft:30,
                color:'black'
            }}>Address</Text>
            <Icon name="chevron-forward-outline" size={20} color='black' style={{
                marginLeft: 190
            }}/>
            </View>
            <TouchableOpacity onPress={()=>navigation.navigate('Login')}>
            <View style={styles.detail}>
            <Icon name="log-out-outline" size={30} color='black' style={{
                marginLeft:20,
            }}/>
            <Text style={{
                fontSize:20,
                marginLeft:30,
                color:'black'
            }}>Sign out</Text>
            <Icon name="chevron-forward-outline" size={20} color='black' style={{
                marginLeft: 190
            }}/>
            </View>
            </TouchableOpacity>
        </View>
    </View>
  )
}


const styles = StyleSheet.create({
    comtainer:{
        flex:1,
    },

    header:{
        flex:1,
        flexDirection: 'row',
        backgroundColor:'#F1F1F3',
        alignItems:'center'
    },
    avatar:{
        flex:1,
        flexDirection: 'row',
        alignItems:'center'
    },
    contact:{
        flex:5,
    },
    detail:{
        height:50,
        flexDirection:'row',
        alignItems:'center',
        borderBottomColor:'#DCDFE5',
        borderBottomWidth:1,
    },
    detail1:{
        height:50,
        flexDirection:'row',
        alignItems:'center',
        borderBottomColor:'#DCDFE5',
        borderBottomWidth:1,
        borderTopWidth:1
    }
})