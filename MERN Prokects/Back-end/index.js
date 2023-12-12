const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const multer = require("multer");
const bcrypt = require("bcrypt");
const fs = require("fs");
const path = require("path");

const jwt = require("jsonwebtoken");
const JWT_Secret = "hahahhaha()nchdius125461353?[]hxhhdsuiu";

const main = async () => {
  const uri =
    "mongodb+srv://akbproduct123:akbproduct123@cluster0.xnpbsqm.mongodb.net/library";
  //const dbName = 'library';

  try {
    await mongoose.connect(uri, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connected to MongoDB Atlas");

    const studentSchema = new mongoose.Schema({
      clas: String,
      stuName: String,
      user: String,
      password: String,
    });
    const Students = mongoose.model("Students", studentSchema);

    const booksSchema = new mongoose.Schema({
      clas: String,
      title: String,
      isbn: String,
      file: {
        data: Buffer,
        contentType: String,
      },
    });
    const Books = mongoose.model("Books", booksSchema);

    const noticeSchema= new mongoose.Schema({
      notices:String

    })
    const Notice=mongoose.model('Notices',noticeSchema);
    const nowelsSchema = new mongoose.Schema({
      title: String,
      author: String,
      isbn: String,
      file: {
        data: Buffer,
        contentType: String,
      },
    });
    const Nowels = mongoose.model("Nowels", nowelsSchema);
    const imageSchema=new mongoose.Schema({
      img:String
    })
    const Image= mongoose.model('Image',imageSchema);

    const newAccountSchema = new mongoose.Schema({
      aname: String,
      userId: String,
      email: String,
      apassword: String,
    });
    const AdminAccount = mongoose.model("Admin", newAccountSchema);

    const server = express();
   
    server.use(cors());
    server.use(bodyParser.json({ limit: "10mb" }));
    server.use(bodyParser.urlencoded({ limit: "10mb", extended: true }));

    const upload = multer({ dest: "uploads/" });
    const port = 8080;

    server.post("/demo", upload.single("file"), async (req, res) => {
      try {
        if (req.body.type === "student") {
          const { clas, stuName, user, password } = req.body;
          console.log("Received stuname:", stuName);
          const saltRounds = 10;
          const hashedPassword = await bcrypt.hash(password, saltRounds);

          const existingStudents = await Students.findOne({ clas, user });
          if (existingStudents) {
            return res
              .status(400)
              .json({ error: "This Student has been already added" });
          }
          let students = new Students();
          students.clas = clas;
          students.stuName = stuName;
          students.user = user;
          students.password = hashedPassword;
          const studentData = await students.save();
          res.json({ studentData });
        } else if (req.body.type === "book") {
          const { isbn } = req.body;
          const existingBook = await Books.findOne({ isbn });
          if (existingBook) {
            return res
              .status(400)
              .json({ error: "This book has been already added" });
          }
          let book = new Books();
          book.clas = req.body.clas;
          book.title = req.body.title;
          book.isbn = req.body.isbn;
          book.file.data = fs.readFileSync(req.file.path);
          book.file.contentType = req.file.mimetype;
          const bookData = await book.save();
          res.json({ bookData });

        } else if (req.body.type === "admin") {
          const { aname, userId, email, apassword } = req.body;
          const saltRounds = 10;
          const hashedPassword = await bcrypt.hash(apassword, saltRounds);

          const existingUser= await AdminAccount.findOne({userId});
          if(existingUser){
            return res.status(400).json({error:"This user is already addedd"});
          }
          let admin = new AdminAccount();
          admin.aname = aname;
          admin.userId = userId;
          admin.email = email;
          admin.apassword = hashedPassword;
          const adminData = await admin.save();
          res.json({ adminData });
        } else if (req.body.type === "nowel") {
          const { isbn } = req.body;
          const existingNowels = await Nowels.findOne({ isbn });
          if (existingNowels) {
            return res
              .status(400)
              .json({ error: "This Nowel has been already added" });
          }
          let nowels = new Nowels();
          nowels.title = req.body.title;
          nowels.author = req.body.author;
          nowels.isbn = req.body.isbn;
          nowels.file.data = fs.readFileSync(req.file.path);
          nowels.file.contentType = req.file.mimetype;
          const nowelData = await nowels.save();
          res.json({ nowelData });
        
        }else if(req.body.type === 'notice'){

          let notice=new Notice();
          notice.notices=req.body.notices;
          const noticeData=await notice.save();
          res.json({noticeData});
        }else {
          res.status(400).json({ error: "Invalid request type" });
        }
      } catch (error) {
        res.status(500).json({ error: "An error occurred while saving data" });
      }
    });

    server.get('/noticeget', async(req,res)=>{
      const noticeData= await Notice.find();
      res.send(noticeData);
    })
    server.delete('/noticedel/:id', async(req,res)=>{
      const delId=req.params.id;
      try{
        const deletedNotice= await Notice.findByIdAndRemove(delId);
        res.status(200).json({ message: "Notice Delete Successfully" });
      }catch(error){
        console.log(error);
      }
    })



    server.post('/images',async(req,res)=>{
      const {base64}=req.body;
      try{
        Image.create({img:base64});
        res.send({status:'ok'})
      }catch(error){
        console.log(error);
      }
    })



    server.get('/image',async(req,res)=>{
      try{
        Image.find({}).then(data=>{
          res.send({status:'ok',data:data})
        })
      }catch(error){
        console.log(error);
      }
      
    })
    server.delete('/deleimg/:id', async(req,res)=>{
      try{
        const imgId=req.params.id.trim();
        const deleteImg= await Image.findByIdAndRemove(imgId);
        res.status(200).json({ message: "Img Delete Successfully" });
      }catch(error){
        console.log(error);
      }
    })


    server.get("/students/:selectedValue", async (req, res) => {
      const selectedClass = req.params.selectedValue; // Get the selected class from the URL parameter
      try {
        const students = await Students.find({ clas: selectedClass });

        // Set the response content type to JSON
        res.setHeader("Content-Type", "application/json");

        res.json(students);
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while fetching student data" });
      }
    });

    server.delete("/deletestu/:id", async (req, res) => {
      try {
        const userId = req.params.id.trim();
        const deleteStu = await Students.findByIdAndRemove(userId);
        if (!deleteStu) {
          return res.status(404).json({ error: "Student not found" });
        }
        res.status(200).json({ message: "Student Delete Successfully" });
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while deleting the Student" });
      }
    });

    server.get("/books/:selectedValue", async (req, res) => {
      const selectedClass = req.params.selectedValue; // Get the selected class from the URL parameter
      try {
        const books = await Books.find({ clas: selectedClass });

        res.setHeader("Content-Type", "application/json");
        res.json(books);
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while fetching student data" });
      }
    });

    server.delete("/deletebook/:id", async (req, res) => {
      try {
        const bookId = req.params.id.trim();
        const deleteBook = await Books.findByIdAndRemove(bookId);
        if (!deleteBook) {
          return res.status(404).json({ error: "Book not found" });
        }
        res.status(200).json({ message: "Book Delete Successfully" });
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while deleting the Book" });
      }
    });

    server.get("/getallnovels", async (req, res) => {
      try {
        const novelsData = await Nowels.find({}, { _id: 0, isbn: 1, title: 1 });
        res.setHeader("Content-Type", "application/json");
        res.json({ novelsData });
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while getting all novels data" });
      }
    });

    server.delete("/deletegetnovels/:isbn", async (req, res) => {
      try {
        const nowelIsbn = req.params.isbn.trim();

        const deleteNowels = await Nowels.findOneAndRemove({ isbn: nowelIsbn });

        if (!deleteNowels) {
          return res.status(404).json({ error: "Nowels not found" });
        }
        res.status(200).json({ message: "Nowels Delete Successfully" });
      } catch (error) {
        res
          .status(500)
          .json({ error: "An error occurred while deleting the Nowels" });
      }
    });

    server.post("/login-user", async (req, res) => {
      const { userId, apassword } = req.body;
      const user = await AdminAccount.findOne({ userId });
      if (!user) {
        return res.json({ error: "User Not Found " });
      }
      if (await bcrypt.compare(apassword, user.apassword)) {
        const token = jwt.sign({ id: user._id }, JWT_Secret);

        if (res.status(201)) {
          return res.json({
            status: "ok",
            data: { token, userId: user.userId },
          });
        } else {
          return res.json({ error: "error" });
        }
      }
      res.json({ status: "error", error: "Invalid password" });
    });

    server.listen(port, () => {
      console.log("Server running on port", port);
    });

    // Close the connection when the server is stopped
    process.on("SIGINT", async () => {
      await mongoose.connection.close();
      console.log("Connection to MongoDB Atlas closed");
      process.exit(0);
    });
  } catch (err) {
    console.error("Error connecting to MongoDB Atlas:", err);
  }
};

main().catch(console.error);
