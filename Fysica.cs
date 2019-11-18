using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Fysica : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public Vector3 startForce;
    public int mass;
    public int stretch;
    public int gravity; 
    
    void Start()
    {
        Force = new Vector3(0,-1,0);
        mass = 5;
        stretch = 100;
        gravity = 1;
    }
    void FixedUpdate()
    {
        Force = -stretch * transform.position + -gravity * Velocity; //veerbeweging toevoegen
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity *Time.deltaTime;
    }
}
