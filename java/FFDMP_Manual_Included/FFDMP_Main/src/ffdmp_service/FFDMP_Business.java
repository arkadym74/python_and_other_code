/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ffdmp_service;

/**
 *
 * @author Arkady Menikhes
 */
public final class FFDMP_Business 
{
    private String customerName;
    private String customerAddress;
    private String flooringType;
    private double floorArea;
    private double floorCost;
    private double cost_per_square_feet;
    

    public FFDMP_Business()//default constructor 
    {
      customerName = "";
      customerAddress = "";
      flooringType = "";
      floorArea = 0.0;
      floorCost = 0.0;
    }
    //Parametarised constructor
    public FFDMP_Business(String cname, String caddress, String ftype, double farea, double fcost)
    {
     this.setcustName(cname);
     this.setcustAddress(caddress);
     this.setfloorType(ftype);
     this.setfloorArea(farea);
     this.setfloorCost(fcost);
    }

    
    //Accessors and mutators
    public void setcustName(String cname) 
    {
        
        this.customerName = cname;
    }
    
    public String getcustName()
    {
    
       return customerName;
    }
    
    public void setcustAddress(String caddress)
    {
    
       this.customerAddress = caddress;
    
    }
    
    public String getcustAddress()
    {
    
      return customerAddress;
    
    }
    
    public void setfloorType(String ftype)
    {
      
      this.flooringType = ftype;
    }
    
    public String getfloorType()
    {
    
       return flooringType;
    }
    
    public void setfloorArea(double farea)
    {
    
      this.floorArea = farea;
    
    }
    
    public double getfloorArea()
    {
       
        return floorArea;
    }
    public double calculateArea(double width, double length)
    {
            
       double area = width * length;
       return area;
      
    }
    public void setfloorCost(double fcost)
    {
    
        this.floorCost = fcost;
    
    }
    public double calculateCost(double floorarea)
    {
        cost_per_square_feet = 0.50;
        
        double cost = cost_per_square_feet * floorarea;
        Math.round(cost);
        return cost;
    }
    public double getfloorCost()
    {
        
        return floorCost;
    
    
    }
    
    @Override
    public String toString()
    {
      return this.getcustName();
    }

}
