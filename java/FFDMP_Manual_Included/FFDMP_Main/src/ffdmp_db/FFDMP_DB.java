/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ffdmp_db;
import ffdmp_service.FFDMP_Business;
import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;


/**
 *
 * @author Arkady Menikhes
 */
public class FFDMP_DB 
{
        private final String url = "jdbc:mysql://localhost:3306/flooring";
        private final String login = "root";
        private final String password = "ArM35643774";
        private Connection conn;
        private PreparedStatement insertStmt;
        private PreparedStatement selectbyname_Stmt;
        private Statement selectall_Stmt;
        private String selectbynameStmt;
        private ResultSet resultsbyname;
        private ResultSet resultsall;
        private final String driverLoad = "com.mysql.jdbc.Driver";
        private final String insertSQL = "INSERT INTO flooring(CustomerName, CustomerAddress, FloorType, FloorArea, FloorCost) values(?,?,?,?,?)";
        private String cname, caddress, ftype;
        private double farea, fcost;
        
        
        public void FFDMPDB()//Database method to connect to a database and load a driver
        {
        try
        {
            try {
                Class.forName(driverLoad);
                
            } catch (ClassNotFoundException ex) {
                Logger.getLogger(FFDMP_DB.class.getName()).log(Level.SEVERE, null, ex);
            }
            //DB connection
            conn = DriverManager.getConnection(url, login, password);
            System.out.println("Loaded Driver and Connected successfully to database");
        }
        catch (SQLException ex)
        {
            ex.printStackTrace();
            System.out.println("Database error");
        }
        }//end of FFDMPDB method
        
        public void insertflooringInfo(FFDMP_Business flb)
        {
          FFDMPDB();
          {
              try
                {
                    //Preparing insert into table
                    insertStmt = conn.prepareStatement(insertSQL);
                    insertStmt.setString(1, flb.getcustName());
                    insertStmt.setString(2, flb.getcustAddress());
                    insertStmt.setString(3, flb.getfloorType());
                    insertStmt.setDouble(4, flb.getfloorArea());
                    insertStmt.setDouble(5, flb.getfloorCost());
                    
                    
                    //executing insert
                    insertStmt.execute();
                    
                    //Closing connection to prevent memory leak.
                    conn.close();
                    JOptionPane.showMessageDialog(null,"Data has been entered successfuly");
                    } catch (SQLException ex) {
                    Logger.getLogger(FFDMP_DB.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
              
        }
        
        public List<FFDMP_Business> retrieveintolistByName(String cname)
        {
         FFDMPDB();
         ArrayList FFDMP_ret_by_name = new ArrayList();
         
         try
         {
                selectbynameStmt = "SELECT * FROM flooring";
                selectbyname_Stmt = conn.prepareStatement(selectbynameStmt);
                resultsbyname = selectbyname_Stmt.executeQuery();
                
          while(resultsbyname.next())
                {
                  cname = resultsbyname.getString("CustomerName");
                  caddress = resultsbyname.getString("CustomerAddress");
                  ftype = resultsbyname.getString("FlooringType");
                  farea = resultsbyname.getDouble("FloorArea");
                  fcost = resultsbyname.getDouble("FloorCost");
                  
                  //Student_Business sb = new Student_Business();
                  FFDMP_Business ffdb = new FFDMP_Business(cname, caddress,ftype,farea,fcost);
                  FFDMP_ret_by_name.add(ffdb);
                  System.out.println("You have retrieved" + cname);
             
                  
                  
                }
                //Closing connection to prevent memory leak.
                conn.close();
                System.out.println("Connection Closed");
         
         
         } catch (SQLException ex) 
          {
                  Logger.getLogger(FFDMP_DB.class.getName()).log(Level.SEVERE, null, ex);
          }
          return FFDMP_ret_by_name;
         
     } 
}